from django.urls import path
from .views import AdgroupListAPIView, TopSearchByRoasForCampaignByStructureValue

app_name = 'ad_api'

urlpatterns = [
    path('', AdgroupListAPIView.as_view(), name='adgroup'),
    path('structure_value/<int:id>/<str:value>/', TopSearchByRoasForCampaignByStructureValue, name='structure_value'),
]