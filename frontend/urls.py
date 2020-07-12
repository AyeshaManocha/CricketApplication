from django.urls import path
from frontend.views import *
app_name = 'frontend'
urlpatterns = [
    path('', teamPage, name='teamspage'),
    path('<int:team_id>/', teamDetailPage, name='detailpage'),
    path('match_fixture/', matchFixtureView, name='match_fixture'),
]