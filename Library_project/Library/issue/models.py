from django.db import models
from registration.models import User

class Book(models.Model):
    book_name = models.CharField(max_length=30, null=True,blank=True)
    author_name = models.CharField(max_length=20, null=True,blank=True)



    def __str__(self):
        return str(self.book_name)

class UserIssuing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.user)