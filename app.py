from flask import Flask, request, render_template, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate-stats', methods=['POST'])
def calculate_stats():
    year = int(request.form['year'])
    month = int(request.form['month'])
    day = int(request.form['day'])
    
    birthdate = datetime(year, month, day)
    now = datetime.now()
    current_age = (now - birthdate).days // 365
    change = now - birthdate

    # STATS CALCULATION (same as before)
    days_alive = int(change.days)
    hours_alive = int(change.total_seconds() // 3600)
    minutes_alive = int(change.total_seconds() // 60)
    seconds_alive = int(change.total_seconds())
    breaths_taken = int(seconds_alive * 0.2)
    heartbeats = int(seconds_alive * 1.3)
    smiles = int(seconds_alive * .00035)
    meals_eaten = int(days_alive * 3)
    steps_taken = int(days_alive * 3700)
    days_slept = int(days_alive * 0.3333)
    earth_distance = int(seconds_alive * 18)
    full_moons = int(days_alive * 0.0339)
    global_rainfall_feet = int(days_alive * 0.0089)
    earthquakes = int((days_alive / 365) * 1400)
    species_discovered = int((days_alive / 365) * 300)
    new_words_added = int(current_age * 1010)

    olympics_since_birth = (now.year - year) // 2
    if now.month < month or (now.month == month and now.day < day):
        olympics_since_birth -= 1
    olympic_games = olympics_since_birth

    same_day_births = 36_700
    deforestation_reversed_percentage = int(1_000_000 * current_age) / (10_000_000 * current_age) * 100
    ocean_rise = ((days_alive / 365) * 0.0131)
    
    if current_age < 18:
        hours_worked = 0
    elif current_age < 26:
        hours_worked = 20 * 52 * (current_age - 18)
    else:
        hours_worked = (20 * 52 * 7) + (40 * 52 * (current_age - 26))

    poverty_lifted = int(current_age * 4_000_000)
    poverty_decrease_percentage = 75
    people_cured = int(current_age * 20_000_000)

    stats = {
        "days_alive": days_alive,
        "hours_alive": hours_alive,
        "minutes_alive": minutes_alive,
        "seconds_alive": seconds_alive,
        "breaths_taken": breaths_taken,
        "heartbeats": heartbeats,
        "smiles": smiles,
        "meals_eaten": meals_eaten,
        "steps_taken": steps_taken,
        "days_slept": days_slept,
        "earth_distance": earth_distance,
        "full_moons": full_moons,
        "global_rainfall_feet": global_rainfall_feet,
        "earthquakes": earthquakes,
        "species_discovered": species_discovered,
        "new_words_added": new_words_added,
        "olympic_games": olympic_games,
        "same_day_births": same_day_births,
        "deforestation_reversed_percentage": deforestation_reversed_percentage,
        "ocean_rise": ocean_rise,
        "hours_worked": hours_worked,
        "poverty_lifted": poverty_lifted,
        "poverty_decrease_percentage": poverty_decrease_percentage,
        "people_cured": people_cured,
    }

    def format_number(number):
        return "{:,}".format(number)
    
    descriptive_stats = {
        'Total days lived': format_number(days_alive),
        'Total hours lived': format_number(hours_alive),
        'Total minutes lived': format_number(minutes_alive),
        'Total seconds lived': format_number(seconds_alive),
        'Total Breaths Taken': format_number(breaths_taken),
        'Heartbeats': format_number(heartbeats),
        'The amount of times you have smiled': format_number(smiles),
        'Meals Eaten': format_number(meals_eaten),
        'Steps Taken': format_number(steps_taken),
        'Days Slept': format_number(days_slept),
        'Distance you travelled with the earth!': format_number(earth_distance),
        'Full Moons Since your Birth': format_number(full_moons),
        'Global Rainfall': format_number(global_rainfall_feet),
        'Earthquakes since birth': format_number(earthquakes),
        'New species discovered': format_number(species_discovered),
        'New Words Added to the dictionary': format_number(new_words_added),
        'Olympic Games Since Birth': format_number(olympic_games),
        'Amount of people with the same birthday!': format_number(same_day_births),
        'Deforestation Reversed': f"{deforestation_reversed_percentage:.2f}%",
        'Ocean Rise': format_number(ocean_rise),
        'Hours you have Worked ': format_number(hours_worked),
        'Poverty Lifted': format_number(poverty_lifted),
        'Poverty Decrease': f"{poverty_decrease_percentage}%",
        'People cured from disease': format_number(people_cured),
    }

    return jsonify(descriptive_stats)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
