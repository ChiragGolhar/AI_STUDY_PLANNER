from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/study-plan", methods=["POST"])
def study_plan():

    data = request.json

    subjects = data["subjects"]
    total_hours = int(data["hours"])
    hard = data["hard"].lower()
    big = data["big"].lower()

    subjects_list = subjects.replace(",", " ").split()

    weights = {}

    for s in subjects_list:

        weight = 1

        if s.lower() == hard:
            weight += 2

        if s.lower() == big:
            weight += 1

        weights[s] = weight

    total_weight = sum(weights.values())

    plan = []

    for subject in subjects_list:

        hours = round((weights[subject] / total_weight) * total_hours, 2)

        plan.append({
            "subject": subject,
            "hours": hours
        })

    # Create timetable
    timetable = []
    start_time = 9

    for item in plan:

        timetable.append({
            "subject": item["subject"],
            "time": f"{start_time}:00 - {start_time + int(item['hours'])}:00"
        })

        start_time += int(item["hours"])

    return jsonify({
        "plan": plan,
        "timetable": timetable
    })


app.run(debug=True)