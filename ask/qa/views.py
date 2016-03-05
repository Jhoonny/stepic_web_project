from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpRequest

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

