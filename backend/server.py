"""
Temporäres Demo-Backend mit Flask für Python 3.14 Kompatibilität.
Stellt die identische REST API wie FastAPI bereit.
Für das finale Projekt: Python 3.12 installieren und FastAPI verwenden.
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

DB_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(DB_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def get_next_id(tasks):
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1


@app.route("/")
def root():
    return jsonify({"message": "Willkommen zur Aufgabenlöscher API", "version": "1.0.0"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(load_tasks())


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    tasks = load_tasks()
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"detail": "Aufgabe nicht gefunden"}), 404
    return jsonify(task)


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    tasks = load_tasks()
    new_task = {
        "id": get_next_id(tasks),
        "title": data.get("title", ""),
        "description": data.get("description", ""),
        "completed": data.get("completed", False)
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify(new_task), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    tasks = load_tasks()
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"detail": "Aufgabe nicht gefunden"}), 404
    if "title" in data:
        task["title"] = data["title"]
    if "description" in data:
        task["description"] = data["description"]
    if "completed" in data:
        task["completed"] = data["completed"]
    save_tasks(tasks)
    return jsonify(task)


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"detail": "Aufgabe nicht gefunden"}), 404
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return jsonify({"message": "Aufgabe erfolgreich gelöscht"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
