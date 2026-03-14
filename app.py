from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/study-plan", methods=["POST"])
def study_plan():

    data = request.json

    subjects = data["subjects"].split(",")
    hours = int(data["hours"])

    per_subject = max(1, hours // len(subjects))

    plan = []

    for s in subjects:
        plan.append({
            "subject": s.strip(),
            "hours": per_subject
        })

    return jsonify(plan)

if __name__ == "__main__":
    app.run(debug=True)