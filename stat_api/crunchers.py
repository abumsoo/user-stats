import re


def get_counts(data_json):
    counts = {
        "females": 0,
        "males": 0,
        "first_am_count": 0,
        "first_nz_count": 0,
        "last_am_count": 0,
        "last_nz_count": 0,
        "states": {},
        "female_population": {},
        "male_population": {},
        "age_range": [0] * 6,
    }
    for p in data_json["results"]:
        state = p["location"]["state"]
        if p["gender"] == "female":
            counts["females"] += 1
            if state in counts["female_population"]:
                counts["female_population"][state] += 1
            else:
                counts["female_population"][state] = 1
        elif p["gender"] == "male":
            counts["males"] += 1
            if state in counts["male_population"]:
                counts["male_population"][state] += 1
            else:
                counts["male_population"][state] = 1

        if re.search(r"^[A-M]", p["name"]["first"][0]):
            counts["first_am_count"] += 1
        elif re.search(r"^[N-Z]", p["name"]["first"][0]):
            counts["first_nz_count"] += 1

        if re.search(r"^[A-M]", p["name"]["last"][0]):
            counts["last_am_count"] += 1
        elif re.search(r"^[N-Z]", p["name"]["last"][0]):
            counts["last_nz_count"] += 1

        if state in counts["states"]:
            counts["states"][state] += 1
        else:
            counts["states"][state] = 1

        age = p["dob"]["age"]
        if age >= 0 and age <= 20:
            counts["age_range"][0] += 1
        elif age >= 21 and age <= 40:
            counts["age_range"][1] += 1
        elif age >= 41 and age <= 60:
            counts["age_range"][2] += 1
        elif age >= 61 and age <= 80:
            counts["age_range"][3] += 1
        elif age >= 81 and age <= 100:
            counts["age_range"][4] += 1
        else:
            counts["age_range"][5] += 1

    return counts


def top_states(states, n, total):
    """
    Returns top 'n' states and their percents
    """
    sorted_states_keys = sorted(states, key=states.get, reverse=True)
    top_n = {}
    for key in sorted_states_keys[0:n]:
        top_n[key] = round(states[key] / total * 100, 2)
    return top_n


def percent_per_state(top_states, population, states_count):
    """
    Returns the percentage of a type of population for each state in top_states
    """
    percentages = {}
    for key in top_states:
        if key in population:
            percentages[key] = round(population[key] / states_count[key] * 100, 2)
        else:
            percentages[key] = 0
    return percentages


def all_stats(counts, total):
    """
    Returns a dictionary with all the statistics
    TODO: separate into smaller functions
    TODO: build dictionary on the go
    """
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

    ranges = ["0-20", "21-40", "41-60", "61-80", "81-100", "100+"]
    age_range = dict(
        zip(ranges, list(map(lambda x: round(x / total * 100, 2), counts["age_range"])))
    )

    return {
        "female_percent": female_percent,
        "male_percent": male_percent,
        "first_am_percent": first_a_m_percent,
        "first_nz_percent": first_n_z_percent,
        "last_am_percent": last_a_m_percent,
        "last_nz_percent": last_n_z_percent,
        "top_ten": top_ten,
        "female_per_state": females_in_top_ten,
        "male_per_state": males_in_top_ten,
        "age_range": age_range,
    }
