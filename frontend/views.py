from django.shortcuts import render
import requests
import json


# Create your views here.
def teamPage(request):
    url = requests.get('http://127.0.0.1:8000/backend/teams/', None)
    return render(request, 'cricketmain/teams.html', {'teams' : json.loads(url.text)})

def teamDetailPage(request, team_id):
    url = requests.get('http://127.0.0.1:8000/backend/team/{team_id}/'.format(team_id=team_id), None)
    return render(request, 'cricketmain/teamdetail.html',{'teamdetail': json.loads(url.text)})

def matchFixtureView(request):
    url = requests.get('http://127.0.0.1:8000/backend/match_fixture/', None)
    res = json.loads(url.text)
    return render(request, 'cricketmain/match_fixture.html',{'match_fixture': res['matches'],'points':res['points']})