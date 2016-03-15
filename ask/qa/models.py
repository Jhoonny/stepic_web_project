from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateField(null=True, auto_now_add=True)
  rating = models.IntegerField(null=True, default=0)
  author = models.ForeignKey(User, default=1, related_name='+')
  likes = models.ManyToManyField(User)

  def __unicode__(self):
    return self.title

  def get_url(self):
    return '/question/%d/' % self.pk


class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateField(null=True, auto_now_add=True)
  question = models.ForeignKey(Question, default=1)
  author = models.ForeignKey(User, default=1, related_name='+')

  def __unicode__(self):
    return self.text

  def get_url(self):
    return '/question/%s/' % self.question
