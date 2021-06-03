from django.shortcuts import render
from django.http import HttpResponse

import json
from stat_api.crunchers import get_counts, all_stats

# Create your views here.
def index(request):
    if request.method == "POST":
        if len(request.FILES) > 0:
            data_json = json.loads(
                request.FILES["input_file"].read()
            )  # change read() to chunks() for scalability
        elif len(request.POST["input_text"]) > 0:
            data_json = json.loads(request.POST["input_text"])
        else:
            return render(request, "stats/index.html")

        stats_json = all_stats(get_counts(data_json), len(data_json["results"]))

        return render(
            request,
            "stats/index.html",
            {
                "female_percent": stats_json["female_percent"],
                "male_percent": stats_json["male_percent"],
                "first_am_percent": stats_json["first_am_percent"],
                "first_nz_percent": stats_json["first_nz_percent"],
                "last_am_percent": stats_json["last_am_percent"],
                "last_nz_percent": stats_json["last_nz_percent"],
                "top_ten": json.dumps(stats_json["top_ten"]),
                "female_per_state": json.dumps(stats_json["female_per_state"]),
                "male_per_state": json.dumps(stats_json["male_per_state"]),
                "age_range": json.dumps(stats_json["age_range"]),
                "birthdays": json.dumps(stats_json["birthdays"]),
            },
        )
    return render(request, "stats/index.html")
