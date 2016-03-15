from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateField(null=True, auto_now_add=True)
  rating = models.IntegerField(null=True, default=0)
  author = models.ForeignKey(User, related_name='user_author', null=True, default=1)
  likes = models.ManyToManyField(User, related_name='user_likes', null=True)

  def __unicode__(self):
    return self.title


class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateField(null=True, auto_now_add=True)
  question = models.ForeignKey(Question, null=True, default=1)
  author = models.ForeignKey(User, null=True, default=1)

  def __unicode__(self):
    return self.text
