from django.shortcuts import render
from .models import SearchTerm

# Create your views here.
def index(request):
    # Retrieve Top Search By Roas For (1578411800 - Nike) Campaign
    structureValues = SearchTerm.objects.filter(campaign_id=1578411800)[:10]
    return render(request, 'index.html', {'structureValues': structureValues})

def login(request):
    return render(request, 'login.html')