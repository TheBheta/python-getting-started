from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    key_word = models.CharField(max_length=100, default="apple")
    finished = models.BooleanField(default=False)
    host = models.CharField(max_length=100, default="")
    winner = models.CharField(max_length=100, default="")

class Guess(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    guess = models.CharField(max_length=100, default = "")
    closest = models.CharField(max_length=100, default = "")
    correct = models.BooleanField(default=False)
    when = models.DateTimeField("date created", auto_now_add=True)

class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, default = "")
    message = models.CharField(max_length=255, default="")
    when = models.DateTimeField("timestamp", auto_now_add=True)