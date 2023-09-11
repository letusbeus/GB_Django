from django.db import models
from django.db.models import Manager, Model


class Author(Model):
    objects = Manager()

    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mail = models.EmailField()
    bio = models.TextField()
    bdate = models.DateField()

    @property
    def get_fullname(self):
        return f'{self.name} {self.lastname}'

    def __str__(self):
        return f'Author: {self.get_fullname}, email: {self.mail}, biography: {self.bio}, date of birth: {self.bdate}'


class Article(Model):
    objects = Manager()

    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'Article: "{self.title}" by {self.author.get_fullname}, {self.date}, published: {self.published}'
