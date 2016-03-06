from django.db import models
# from django.contrib.auth import models

class Question(models.User):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField(blank=True)
  rating = models.IntegerField()
  author = models.CharField(max_length=50)

  likes = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

  def __unicode__(self):
    return self.title
  def get_absolute_url(self):
    return '/question/%d/' % self.pk

  class Meta:
    db_table = 'qa_question'
    ordering = ['-creation_date']


class Answer(models.User):
  text = models.TextField()
  added_at = models.DateTimeField(blank=True)
  author = models.CharField(max_length=50)
  question =

  status = models.OneToOneField(PostStatus)
  tags = models.ManyToManyField(Tag)
