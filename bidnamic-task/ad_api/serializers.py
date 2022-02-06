from rest_framework import serializers
from ad.models import Adgroup, SearchTerm, Campaign

class AdgroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adgroup
        fields = '__all__'

class SearchTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchTerm
        fields = '__all__'
        depth = 1

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'
        depth = 1
