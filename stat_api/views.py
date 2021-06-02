from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from stat_api.models import Stats
from stat_api.serializers import StatsSerializer
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from stat_api.crunchers import get_counts, top_states, percent_per_state, all_stats

# Create your views here.
@csrf_exempt
def stats_list(request):
    if request.method == "GET":
        stats = Stats.objects.all()
        serializer = StatsSerializer(stats, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data_json = JSONParser().parse(request)
        return JsonResponse(all_stats(get_counts(data_json), len(data_json["results"])))
