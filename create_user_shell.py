"""
python manage.py shell
from django.contrib.auth.models import User
user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword').save().

ну и в формс должно быть прописан айди:
def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 1
        question.save()
        return question

"""