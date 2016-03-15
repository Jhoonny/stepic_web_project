from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST

# Create your views here.

from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, Signup, Login
from django.contrib.auth import authenticate, login


def index(request):
    posts = Question.objects.order_by('-id')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page) # Page

    return render(request, 'last_questions_on_main.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def popular(request):
    try:
        posts = Question.objects.order_by('-rating')
    except Question.DoesNotExist:
        raise Http404

    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page) # Page

    return render(request, 'last_questions_on_main.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


#@require_GET
def detail(request, id):
    question = get_object_or_404(Question, id=id)
    question.answer_set.all()

    return render(request, 'question.html', {
        'question': question,
        'form': AnswerForm(initial={'question': question.id}),
    })


def add_question(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask_form.html', {
        'form': form
    })


#@require_POST
def add_answer(request):
    url = ''
    if request.method == "POST":
        form = AnswerForm(request.POST)
        form._user = request.user
        if form.is_valid():
            answer = form.save()
            url = answer.get_url()
            return redirect('detail', id=answer.question.id)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def signup(request):
    if request.method == "POST":
        form = Signup(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = Signup()
    return render(request, 'user/signup.html', {
        'form': form
    })


def auth_login(request):
    if request.method == "POST":
        form = Login(request)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                # Return a 'disabled account' error message
                return render(request, 'login.html',
                {'form': form, 'message': 'disabled account'})
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html',
            {'form': form, 'message': 'invalid login'})
    else:
        form = Login()
    return render(request, 'user/login.html', {
        'form': form
    })



def test():
    return "ok"