import random
import itertools
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class TeamView(APIView):
    def get(self, request, format = None):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many = True)
        return Response(serializer.data)

class TeamDetailView(APIView):
    def get(self, request, team_id, format = None):
        players = Player.objects.select_related('team').filter(team__id = team_id)
        serializer = TeamDetailSerializer(players, many = True)
        return Response(serializer.data)

class MatchFixture(APIView):
    def get(self, request, format = None):
        teams = Team.objects.all()
        pairs = list(itertools.combinations(teams, 2))
        random.shuffle(pairs)
        result = []
        count = 0
        points_dict = {}
        for team_name in teams:
            points_dict[team_name.name] = 0
        
        for i in pairs:
            temp = {}
            count += 1
            temp['matchnumber'] = count
            temp['teamone'] = i[0].name
            temp['teamtwo'] = i[1].name
            temp['winner'] = random.choice([temp['teamone'],temp['teamtwo']])
            points_dict[temp['winner']] += 5
            result.append(temp)
        sort_points = sorted(points_dict.items(), key=lambda x: x[1], reverse=True)
        rank = 1
        sort_points_out = []
        for i in sort_points:
            out_points = {}
            out_points['rank'] = rank
            out_points['team_name'] = i[0]
            out_points['points'] = i[1]
            rank += 1
            sort_points_out.append(out_points)

        serializer = MatchFixtureSerializer(result, many = True)
        response_api = {'matches':serializer.data, 'points':sort_points_out}
        return Response(response_api)
