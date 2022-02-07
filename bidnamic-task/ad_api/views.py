from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from ad.models import SearchTerm
from .serializers import SearchTermSerializer
from datetime import datetime

# Create your views here.
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def index(request):
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message = 'Clock In server is live current time is'
    return Response(data=message + date, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def TopSearchByRoasForCampaignByStructureValue(request, value, id):
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

