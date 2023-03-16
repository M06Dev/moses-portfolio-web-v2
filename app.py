from flask import Flask, render_template, jsonify
from database import load_projects_from_db

app = Flask(__name__)

# projects = [
#     {
#         "pj": 1,
#         "title": "Ultrasound Report Generator",
#         "Description": "this website does so so so...",
#     },
#     {"pj": 2, "title": "Wallet", "Description": "this website does so so so..."},
#     {"pj": 3, "title": "Medical Jobs", "Description": "this website does so so so..."},
#     {
#         "pj": 4,
#         "title": "Medical Website",
#         "Description": "this website does so so so...",
#     },
# ]


@app.route("/")
def hello_world():
    projects = load_projects_from_db()
    return render_template("home.html", projs = projects)


@app.route("/api/projects")
def list_projects():
    return jsonify(projects)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
