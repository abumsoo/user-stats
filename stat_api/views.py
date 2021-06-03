from django.http import JsonResponse
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from stat_api.crunchers import get_counts, all_stats
from dict2xml import dict2xml

# Create your views here.
@csrf_exempt
def stats_list(request):
    if request.method == "POST":
        data_json = JSONParser().parse(request)
        stats_json = all_stats(get_counts(data_json), len(data_json["results"]))
        if request.headers["Accept"] == "application/json":
            return JsonResponse(stats_json)
        elif request.headers["Accept"] == "application/xml":
            stats_xml = dict2xml(stats_json)
            return HttpResponse(stats_xml, content_type="application/xml")
        elif request.headers["Accept"] == "text/plain":
            stats_txt = "Percentage female versus male: {} vs {}\n".format(
                stats_json["female_percent"],
                stats_json["male_percent"],
            )
            stats_txt += "Percentage of first names that start with A-M versus N-Z: {} vs {}\n".format(
                stats_json["first_am_percent"],
                stats_json["first_nz_percent"],
            )
            stats_txt += "Percentage of last names that start with A-M versus N-Z: {} vs {}\n".format(
                stats_json["last_am_percent"],
                stats_json["last_nz_percent"],
            )
            stats_txt += (
                "Percentage of people in each state in top 10 most populous states:\n"
            )
            for key in stats_json["top_ten"]:
                stats_txt += "{}: {}%\n".format(key, stats_json["top_ten"][key])
            stats_txt += (
                "Percentage of females in each state in top 10 most populous states:\n"
            )
            for key in stats_json["female_per_state"]:
                stats_txt += "{}: {}%\n".format(
                    key, stats_json["female_per_state"][key]
                )
            stats_txt += (
                "Percentage of males in each state in top 10 most populous states:\n"
            )
            for key in stats_json["male_per_state"]:
                stats_txt += "{}: {}%\n".format(key, stats_json["male_per_state"][key])
            stats_txt += "Percentage of people in age ranges:\n"
            for key in stats_json["age_range"]:
                stats_txt += "{}: {}%\n".format(key, stats_json["age_range"][key])

            return HttpResponse(stats_txt, content_type="text/plain")
