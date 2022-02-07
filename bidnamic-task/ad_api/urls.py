from django.urls import path
from .views import index, TopSearchByRoasForCampaignByStructureValue

app_name = 'ad_api'

urlpatterns = [
    path('checkserver', index, name='index'),
    path('structure_value/<str:value>/<int:id>/', TopSearchByRoasForCampaignByStructureValue, name='structure_value'),
]