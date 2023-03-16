from flask import Flask, render_template, jsonify
from database import load_projects_from_db

app = Flask(__name__)

@app.route("/")
def hello_world():
    projects = load_projects_from_db()
    return render_template("home.html", projs = projects)


@app.route("/api/projects")
def list_projects():
    projects = load_projects_from_db()
    return jsonify(projects)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
