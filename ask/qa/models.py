from django.db import models
from django.http import Http404
from django.contrib.auth.models import User

class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField(null=False, auto_now_add=True)
  rating = models.IntegerField(null=False, default=0)
  author = models.ForeignKey(User, related_name='question_author', null=True)
  likes = models.ManyToManyField(User, related_name='question_likes', null=True)

  def __unicode__(self):
    return self.title

  def get_absolute_url(self):
    return "/question/%d/" % self.id

  class Meta:
    db_table = 'question'
    ordering = ['-creation_date']


class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(null=False, auto_now_add=True)
  question = models.ForeignKey(Question)
  author = models.ForeignKey(User, related_name='answer_author', null=True)

  def __unicode__(self):
    return self.text

class QuestionManager(models.Manager):
    def get_questions_by_type(self, question_type):
        if question_type == "" or question_type == "new":
            return self.order_by("-added_at", "-id")
        elif question_type == "popular":
            return self.order_by("-rating", "-id")
        else:
            raise Http404