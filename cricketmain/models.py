from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.TextField(max_length = 40)
    logo_uri = models.URLField()
    club_state = models.TextField(max_length = 40)

    class Meta:
        db_table = 'team'

class Player(models.Model):
    first_name = models.TextField(max_length = 40)
    last_name = models.TextField(max_length = 40)
    image_uri = models.URLField(max_length = 500)
    jersey_number = models.IntegerField()
    country = models.TextField(max_length = 40)
    history = models.TextField(max_length = 500)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        db_table = 'player'

class Match(models.Model):
    teamone = models.ForeignKey(Team, related_name='teamone', on_delete=models.CASCADE)
    teamtwo = models.ForeignKey(Team, related_name='teamtwo', on_delete=models.CASCADE)
    winner = models.ForeignKey(Team, related_name='winner', on_delete=models.CASCADE)

    class Meta:
        db_table = 'match'

class Point(models.Model):
    points = models.IntegerField(default = 0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        db_table = 'point'