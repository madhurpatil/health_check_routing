import json
import logging
import os
import time
from flask import Flask, jsonify

# ----------------------------------------
# Flask App
# ----------------------------------------

app = Flask(__name__)

logging.basicConfig(
    filename="health_check.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

current_index = 0

# ----------------------------------------
# Statistics Dictionary
# ----------------------------------------

lb_stats = {
    "total_requests": 0,
    "active_tasks": 0,
    "worker_distribution": {},
    "current_worker": None,
    "algorithm": "Round Robin",
    "average_response_time_ms": 0
}

response_times = []


# ----------------------------------------
# Load Server Status
# ----------------------------------------

def load_server_status(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)

    except Exception:
        return {}


# ----------------------------------------
# Healthy Servers
# ----------------------------------------

def get_healthy_servers(server_data):

    healthy = []

    for server, status in server_data.items():

        if status.lower() == "healthy":
            healthy.append(server)

    return healthy


# ----------------------------------------
# Round Robin
# ----------------------------------------

def route_request(healthy_servers):

    global current_index

    if not healthy_servers:
        return None

    start = time.time()

    server = healthy_servers[
        current_index % len(healthy_servers)
    ]

    current_index += 1

    lb_stats["total_requests"] += 1
    lb_stats["current_worker"] = server

    lb_stats["worker_distribution"].setdefault(server, 0)
    lb_stats["worker_distribution"][server] += 1

    lb_stats["active_tasks"] += 1

    time.sleep(0.05)

    lb_stats["active_tasks"] -= 1

    elapsed = (time.time() - start) * 1000

    response_times.append(elapsed)

    lb_stats["average_response_time_ms"] = round(
        sum(response_times) / len(response_times), 2
    )

    logging.info(f"Request routed to {server}")

    return server


# ----------------------------------------
# Route Request API
# ----------------------------------------

@app.route("/route")
def route():

    server_data = load_server_status("server_status.json")

    healthy = get_healthy_servers(server_data)

    server = route_request(healthy)

    return jsonify({
        "server": server
    })


# ----------------------------------------
# Load Balancer Statistics API
# ----------------------------------------

@app.route("/lb/stats")
def load_balancer_stats():

    return jsonify({
        "algorithm": lb_stats["algorithm"],
        "current_worker": lb_stats["current_worker"],
        "total_requests": lb_stats["total_requests"],
        "active_tasks": lb_stats["active_tasks"],
        "average_response_time_ms":
            lb_stats["average_response_time_ms"],
        "worker_distribution":
            lb_stats["worker_distribution"]
    })


# ----------------------------------------
# Healthy Servers API
# ----------------------------------------

@app.route("/healthy")
def healthy():

    data = load_server_status("server_status.json")

    healthy = get_healthy_servers(data)

    return jsonify({
        "healthy_servers": healthy
    })


# ----------------------------------------
# Run Server
# ----------------------------------------

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        use_reloader=False
    )
