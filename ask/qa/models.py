from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(null=True, auto_now_add=True)
    rating = models.IntegerField(null=True)
    author = models.ForeignKey(User, default=1, related_name='+')
    likes = models.ManyToManyField(User)

    def __unicode__(self):
        return self.title

    def get_url(self):
        return '/question/%d/' % self.pk


class Answer(models.Model):
    text = models.CharField(max_length=255)
    added_at = models.DateTimeField(null=True, auto_now_add=True)
    question = models.ForeignKey(Question, null=True)
    author = models.ForeignKey(User, default=1, related_name='+')

    def get_url(self):
        return '/question/%s/' % self.question

    #def __unicode__(self):
        #return self.text