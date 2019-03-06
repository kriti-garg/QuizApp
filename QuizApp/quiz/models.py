from django.db import models

class genres(models.Model):
    content = models.TextField();

class leaderboards(models.Model):
    score = models.IntegerField(default=0)
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    subgenre_id = models.ForeignKey(subgenre, on_delete=models.CASCADE)

class subgenre(models.Model):
    cont = models.TextField()
    genre_id = models.ForeignKey(genre, on_delete=models.CASCADE)

class questions(models.Model):
    ques = models.CharFiels(max_length=200)
    optA = models.TextField()
    optB = models.TextField()
    optC = models.TextField()
    optD = models.TextField()
    correctopt = models.TextField()
    subgenre_id = models.ForeignKey(subgenre, on_delete=models.CASCADE)

class users(models.Model):
    name = models.TextField()
    email = models.EmailField()
    password_digest = models.TextField()
    remember_digest = models.TextField()
    admin = models.BooleanField(default=0)

class states(models.Model):
    subgenre_id = models.ForeignKey(subgenre, on_delete=models.CASCADE)
    users_id = models.ForeignKey(users, on_delete=models.CASCADE)
    qno = IntegerField(default=0)
    score = IntegerField(defalut=0)


