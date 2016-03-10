from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpRequest
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.http import require_GET
from ask.qa.models import Question, Answer

def test(request, *args, **kwargs):
  return HttpResponse('OK')
  # return render(request, "base.html")

def post_text(request):
  try:
    id = request.GET.get('id')
    obj = Post.objects.get(pk=id)
  except Post.DoesNotExist:
    raise Http404
  return HttpResponse(obj.text, content_type='text/plain')

@require_GET
def question_list(request):
  try:
    ask = Question.objects.get()
  except Question.DoesNotExist:
    raise Http404
  return render(request, 'ask/ask_list.html', {
    'ask': ask
  })
