from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)  # Use ObjectIdField for compatibility
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)  # Use ObjectIdField for compatibility
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)  # Changed to ManyToManyField for proper relationship handling

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)  # Use ObjectIdField for compatibility
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True)  # Use ObjectIdField for compatibility
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Added user field as ForeignKey
    points = models.IntegerField()

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True)  # Use ObjectIdField for compatibility
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
