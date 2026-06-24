import json
import logging
import os

# --------------------------------------------------
# Logging Configuration
# --------------------------------------------------

logging.basicConfig(
    filename="health_check.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --------------------------------------------------
# Global Variable For Round Robin
# --------------------------------------------------

current_index = 0

# --------------------------------------------------
# Load Server Status
# --------------------------------------------------

def load_server_status(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        logging.error("Input JSON file not found.")
        return {}

    except Exception as e:
        logging.error(f"Error loading file: {e}")
        return {}

# --------------------------------------------------
# Health Check
# --------------------------------------------------

def get_healthy_servers(server_data):

    healthy_servers = []

    for server, status in server_data.items():

        if status.lower() == "healthy":
            healthy_servers.append(server)
            logging.info(f"{server} is HEALTHY")

        else:
            logging.warning(f"{server} is DOWN")

    return healthy_servers

# --------------------------------------------------
# Round Robin Routing
# --------------------------------------------------

def route_request(healthy_servers):

    global current_index

    if not healthy_servers:
        logging.error("No healthy servers available.")
        return None

    server = healthy_servers[
        current_index % len(healthy_servers)
    ]

    current_index += 1

    logging.info(
        f"Request routed to {server}"
    )

    return server

# --------------------------------------------------
# Save Healthy Servers Output
# --------------------------------------------------

def save_output(healthy_servers):

    os.makedirs("output", exist_ok=True)

    output = {
        "healthy_servers": healthy_servers
    }

    with open(
        "output/healthy_servers.json",
        "w"
    ) as file:

        json.dump(
            output,
            file,
            indent=4
        )

# --------------------------------------------------
# Simulate Multiple Requests
# --------------------------------------------------

def simulate_requests(
        healthy_servers,
        total_requests=10):

    print("\nRouting Requests:\n")

    for i in range(total_requests):

        server = route_request(
            healthy_servers
        )

        print(
            f"Request {i+1} --> {server}"
        )

# --------------------------------------------------
# Main Function
# --------------------------------------------------

def main():

    print(
        "\n===== HEALTH CHECK ROUTING SYSTEM =====\n"
    )

    server_data = load_server_status(
        "server_status.json"
    )

    healthy_servers = get_healthy_servers(
        server_data
    )

    save_output(healthy_servers)

    print(
        "Healthy Servers:",
        healthy_servers
    )

    simulate_requests(
        healthy_servers,
        total_requests=10
    )

# --------------------------------------------------
# Driver Code
# --------------------------------------------------

if __name__ == "__main__":
    main()