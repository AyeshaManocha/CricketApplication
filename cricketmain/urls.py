from django.urls import path
from cricketmain.views import *

urlpatterns = [
    path('teams/', TeamView.as_view(), name='teams'),
    path('team/<int:team_id>/', TeamDetailView.as_view(), name='teamdetail'),
    path('match_fixture/', MatchFixture.as_view(), name='matchfixture'),
]