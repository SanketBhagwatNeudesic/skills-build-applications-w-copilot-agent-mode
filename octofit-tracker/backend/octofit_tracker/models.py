from djongo import models

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None)
    name = models.CharField(max_length=100, unique=True)

class User(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # minutes
    calories = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ManyToManyField(Team)

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
