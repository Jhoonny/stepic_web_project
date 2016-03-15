from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import Question, Answer
from .forms import AskForm, AnswerForm

from django.core.paginator import Paginator


def test(request, *args, **kwargs):
  return HttpResponse("OK")


@csrf_protect
def signup(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = User.objects.create_user(username, email, password)

    user_auth = authenticate(username=username, password=password)
    login(request, user_auth)
    return HttpResponseRedirect('/')
  else:
    return render(request, 'signup.html')


@csrf_protect
def login_user(request):
  error = ''
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      return HttpResponseRedirect('/')
    else:
      error = 'Invalid username/password'
      return HttpResponseRedirect('/login/', {'error': error,})
  else:
    return render(request, 'login.html')


def logout_user(request):
  logout(request)
  return HttpResponseRedirect('/')


def index(request):
  quests = Question.objects.order_by('-id')
  limit = 10
  paginator = Paginator(quests, limit)

  page = request.GET.get('page', 1)
  quests = paginator.page(page)
  paginator.baseurl = '/?page='

  user = request.user

  return render(request, 'index.html', {
    'quest_list': quests,
    'paginator': paginator,
    'page': page,
    'user': user,
  })


def popular_quests(request):
  quests = Question.objects.order_by('-rating')
  limit = 10
  paginator = Paginator(quests, limit)

  page = request.GET.get('page', 1)
  quests = paginator.page(page)
  paginator.baseurl = '/popular/?page='

  return render(request, 'popular.html', {
    'quest_list': quests,
    'paginator': paginator,
    'page': page
  })


@csrf_protect
def one_quest(request, id):
  id = int(id)
  try:
    quest = Question.objects.get(pk=id)
  except Question.DoesNotExist:
    raise Http404
  return render(request, 'details.html', {
    'quest': quest
  })


@csrf_protect
def ask_add(request):
  if request.method == 'POST':
    form = AskForm(request.POST)
    form._user = request.user
    # user = request.user
    # text = request.POST['text']
    # title = request.POST['title']
    # form = AskForm(user, text=text, title=title)

    if form.is_valid():
      ask = form.save()
      # url = '/question/{0}'.format(ask.id)
      url = ask.get_url()
      return HttpResponseRedirect(url)
  else:
    form = AskForm()
  return render(request, 'add_ask.html', {
    'form': form
  })


@csrf_protect
def answer_add(request):
  if request.method == 'POST':
    form = AnswerForm(request.POST)
    if form.is_valid():
      answer = form.save()
      # url = '/question/{0}'.format(answer.question_id)
      url = answer.get_url()
      return HttpResponseRedirect(url)
  else:
    form = AnswerForm()
  return render(request, 'add_answer.html', {
    'form': form
  })
