from rest_framework import serializers

class TeamSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    logo_uri = serializers.CharField(max_length=200)
    club_state = serializers.CharField(max_length=200)

class PlayerSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    image_uri = serializers.CharField(max_length=200)

class TeamDetailSerializer(serializers.Serializer):
    team_name = serializers.CharField(max_length=200)
    players = PlayerSerializer(many = True)

class MatchFixtureSerializer(serializers.Serializer):
    matchnumber = serializers.CharField(max_length=200)
    teamone = serializers.CharField(max_length=200)
    teamtwo = serializers.CharField(max_length=200)
    winner = serializers.CharField(max_length=200)