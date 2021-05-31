from django.shortcuts import render
from django.http import HttpResponse

import json
import re

# Create your views here.
def index(request):

    if request.method == "POST":
        data_json = json.loads(
            request.FILES["input_file"].read()
        )  # change read() to chunks() for scalability

        # gender ratio
        total = len(data_json["results"])
        females = 0
        males = 0
        for p in data_json["results"]:
            if p["gender"] == "female":
                females += 1
            elif p["gender"] == "male":
                males += 1
        female_percent = females / total * 100
        male_percent = males / total * 100

        # first name ratios
        first_a_m_count = 0
        first_n_z_count = 0
        for p in data_json["results"]:
            if re.search(r"^[A-M]", p["name"]["first"][0]):
                first_a_m_count += 1
            elif re.search(r"^[N-Z]", p["name"]["first"][0]):
                first_n_z_count += 1
        first_a_m_percent = first_a_m_count / total * 100
        first_n_z_percent = first_n_z_count / total * 100

        # last name ratios
        last_a_m_count = 0
        last_n_z_count = 0
        for p in data_json["results"]:
            if re.search(r"^[A-M]", p["name"]["last"][0]):
                last_a_m_count += 1
            elif re.search(r"^[N-Z]", p["name"]["last"][0]):
                last_n_z_count += 1
        last_a_m_percent = last_a_m_count / total * 100
        last_n_z_percent = last_n_z_count / total * 100

        # Most populous states
        states = {}
        female_population = {}
        male_population = {}
        for p in data_json["results"]:
            state = p["location"]["state"]
            if state in states:
                states[state] += 1
            else:
                states[state] = 1
            if p["gender"] == "female":
                if state in female_population:
                    female_population[state] += 1
                else:
                    female_population[state] = 1
            elif p["gender"] == "male":
                if state in male_population:
                    male_population[state] += 1
                else:
                    male_population[state] = 1

        sorted_states_keys = sorted(states, key=states.get, reverse=True)
        top_ten = {}
        for key in sorted_states_keys[0:10]:
            top_ten[key] = round(states[key] / total * 100, 2)

        # female percent in each state
        female_per_state = {}
        for key in sorted_states_keys[0:10]:
            female_per_state[key] = round(female_population[key] / states[key] * 100, 2)

        # male percent in each state
        male_per_state = {}
        for key in sorted_states_keys[0:10]:
            male_per_state[key] = round(male_population[key] / states[key] * 100, 2)

        # percentage by age range
        age_range = [0] * 6
        for p in data_json["results"]:
            age = p["dob"]["age"]
            if age >= 0 and age <= 20:
                age_range[0] += 1
            elif age >= 21 and age <= 40:
                age_range[1] += 1
            elif age >= 41 and age <= 60:
                age_range[2] += 1
            elif age >= 61 and age <= 80:
                age_range[3] += 1
            elif age >= 81 and age <= 100:
                age_range[4] += 1
            else:
                age_range[5] += 1
        age_range = list(map(lambda x: round(x / total * 100, 2), age_range))

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
                "female_per_state": json.dumps(female_per_state),
                "male_per_state": json.dumps(male_per_state),
                "age_range": json.dumps(age_range),
            },
        )
    return render(request, "stats/index.html")