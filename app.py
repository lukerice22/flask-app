from flask import Flask, request, render_template, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)

@app.route('/calculate-stats', methods=['POST'])
def calculate_stats():
    try:
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
        
        # Inside your Flask route (calculate_stats):
        descriptive_stats = {
    'Total days lived': f"{format_number(days_alive)} days",
    'Total hours lived': f"{format_number(hours_alive)} hours",
    'Total minutes lived': f"{format_number(minutes_alive)} minutes",
    'Total seconds lived': f"{format_number(seconds_alive)} seconds",
    'Total Breaths Taken': f"{format_number(breaths_taken)} breaths",
    'Heartbeats': f"{format_number(heartbeats)} beats",
    'The amount of times you have smiled': f"{format_number(smiles)} times",
    'Meals Eaten': f"{format_number(meals_eaten)} meals",
    'Steps Taken': f"{format_number(steps_taken)} steps",
    'Days Slept': f"{format_number(days_slept)} days",
    'Distance you travelled with the earth!': f"{format_number(earth_distance)} miles",
    'Full Moons Since your Birth': f"{format_number(full_moons)} full moons",
    'Global Rainfall': f"{format_number(global_rainfall_feet)} feet",
    'Earthquakes since birth': f"{format_number(earthquakes)} earthquakes",
    'New species discovered': f"{format_number(species_discovered)} species",
    'New Words Added to the dictionary': f"{format_number(new_words_added)} words",
    'Olympic Games Since Birth': f"{format_number(olympic_games)} games",
    'Amount of people with the same birthday!': f"{format_number(same_day_births)} people",
    'Deforestation Reversed': f"{deforestation_reversed_percentage:.2f}%",
    'Ocean Rise': f"{ocean_rise:.4f} inches",
    'Hours you have Worked ': f"{format_number(hours_worked)} hours",
    'Poverty Lifted': f"{format_number(poverty_lifted)} people",
    'Poverty Decrease': f"{poverty_decrease_percentage}%",
    'People cured from disease': f"{format_number(people_cured)} people",
}

        return jsonify(descriptive_stats)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
