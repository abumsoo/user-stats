from rest_framework import serializers
from stat_api.models import Stats


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = ["id"]
