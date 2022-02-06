from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, status
from django.shortcuts import render
from ad.models import Adgroup, SearchTerm, Campaign
from .serializers import AdgroupSerializer, SearchTermSerializer, CampaignSerializer

# Create your views here.
# Show time
class AdgroupListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = Adgroup.objects.all()
    serializer_class = AdgroupSerializer

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def TopSearchByRoasForCampaignByStructureValue(request, id, value):
    try:
        if id == 1578411800 and value == 'nike':
            campaign_id = 1578411800
        elif id == 1578629887 and value == 'adidas':
            campaign_id = 1578629887
        elif id == 1578411797 and value == 'nike':
            campaign_id = 1578411797
        elif id == 1578630235 and value == 'puma':
            campaign_id = 1578630235
        else:
            campaign_id = 1578411800

        search_terms = SearchTerm.objects.filter(campaign_id=campaign_id)[:10]
        serializer = SearchTermSerializer(search_terms, many=True)
        return Response(serializer.data)
    except SearchTerm.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

