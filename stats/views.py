from django.shortcuts import render
from django.http import HttpResponse

import json
from stat_api.crunchers import get_counts, top_states, percent_per_state

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

        total = len(data_json["results"])
        counts = get_counts(data_json)

        # gender ratios
        female_percent = counts["females"] / total * 100
        male_percent = counts["males"] / total * 100

        # first name ratios
        first_a_m_percent = counts["first_am_count"] / total * 100
        first_n_z_percent = counts["first_nz_count"] / total * 100

        # last name ratios
        last_a_m_percent = counts["last_am_count"] / total * 100
        last_n_z_percent = counts["last_nz_count"] / total * 100

        # Most populous states
        top_ten = top_states(counts["states"], 10, total)

        # female percent in each state
        females_in_top_ten = percent_per_state(
            top_ten, counts["female_population"], counts["states"]
        )

        # male percent in each state
        males_in_top_ten = percent_per_state(
            top_ten, counts["male_population"], counts["states"]
        )

        age_range = list(map(lambda x: round(x / total * 100, 2), counts["age_range"]))

        return render(
            request,
            "stats/index.html",
            {
                "female_percent": female_percent,
                "male_percent": male_percent,
                "first_am_percent": first_a_m_percent,
                "first_nz_percent": first_n_z_percent,
                "last_am_percent": last_a_m_percent,
                "last_nz_percent": last_n_z_percent,
                "top_ten": json.dumps(top_ten),
                "female_per_state": json.dumps(females_in_top_ten),
                "male_per_state": json.dumps(males_in_top_ten),
                "age_range": json.dumps(age_range),
            },
        )
    return render(request, "stats/index.html")
