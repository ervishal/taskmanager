from flask import Flask, jsonify, request
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

tasks = []
REQUEST_COUNT = Counter('app_requests_total', 'Total Requests')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    REQUEST_COUNT.inc()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    REQUEST_COUNT.inc()
    data = request.json
    # ❌ No validation!
    tasks.append({"id": len(tasks)+1, "title": data["title"]})
    return jsonify({"message": "Task Added"})

@app.route('/tasks/<int:id>/divide')
def divide(id):
    return jsonify({"result": 100/id})  # ❌ CRASH if id=0

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(debug=True, port=5000)