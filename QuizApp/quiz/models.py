from django.db import models
from django import forms

class genres(models.Model):
    content = models.TextField();

class subgenre(models.Model):
    cont = models.TextField()
    genre_id = models.ForeignKey(genres, on_delete=models.CASCADE)

class users(models.Model):
    name = models.TextField()
    email = models.EmailField()
    password_digest = forms.CharField(max_length=32, widget=forms.PasswordInput)
    remember_digest = forms.CharField(max_length=32, widget=forms.PasswordInput)
    admin = models.BooleanField(default=0)

class leaderboards(models.Model):
    score = models.IntegerField(default=0)
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    subgenre_id = models.ForeignKey(subgenre, on_delete=models.CASCADE)

class questions(models.Model):
    ques = models.CharField(max_length=200)
    optA = models.TextField()
    optB = models.TextField()
    optC = models.TextField()
    optD = models.TextField()
    correctopt = models.TextField()
    subgenre_id = models.ForeignKey(subgenre, on_delete=models.CASCADE)


class states(models.Model):
    subgenre_id = models.ForeignKey(subgenre, on_delete=models.CASCADE)
    users_id = models.ForeignKey(users, on_delete=models.CASCADE)
    qno = models.IntegerField(default=0)
    score = models.IntegerField(default=0)


