# Health Check Based Routing System

## Project Information

**Project Title:** Health Check Based Routing System
**Assigned To:** Madhur Patil
**Captain:** Goli Nithin
**Module:** Load Balancing & Scheduling Algorithms
**Difficulty:** Medium
**Duration:** 2–3 Days

---

# Overview

The Health Check Based Routing System is a Python-based load balancing project that monitors server health and routes incoming requests only to healthy servers.

In modern distributed systems, servers may fail due to hardware issues, software crashes, network failures, or maintenance activities. Sending requests to failed servers can lead to downtime and poor user experience.

This project solves that problem by performing health checks on servers before routing traffic. Only active and healthy servers are selected for request processing. The project also uses the Round Robin scheduling algorithm to distribute requests evenly among healthy servers.

---

# Objective

The primary objective of this project is to:

* Monitor server health.
* Detect failed servers.
* Route requests only to healthy servers.
* Implement fault tolerance.
* Simulate load balancing using Round Robin scheduling.
* Generate logs for monitoring and troubleshooting.

---

# Why Health Checks Matter

Health checks are an essential component of modern load balancers.

Without health checks:

* Requests may be sent to unavailable servers.
* Applications may become unreliable.
* User experience may degrade.
* System availability decreases.

With health checks:

* Failed servers are automatically excluded.
* Traffic reaches only active servers.
* System reliability increases.
* Downtime is minimized.

---

# Key Concepts Learned

## Health Check

A mechanism used to determine whether a server is operational and capable of handling requests.

## Server Monitoring

Continuous observation of server status to identify healthy and unhealthy nodes.

## Failure Detection

Detecting server crashes or downtime and preventing traffic from reaching failed servers.

## Routing Decisions

Selecting the appropriate server for processing incoming requests.

## Fault Tolerance

Ensuring system operation continues even if some servers fail.

## Load Balancing

Distributing traffic evenly among multiple healthy servers.

---

# System Architecture

Input JSON
↓
Health Check Engine
↓
Healthy Server Identification
↓
Round Robin Scheduler
↓
Request Routing
↓
Log Generation
↓
Output JSON

---

# Project Structure

health_check_routing/

├── health.py

├── server_status.json

├── health_check.log

├── output/

│ └── healthy_servers.json

├── screenshots/

│ ├── input.png

│ ├── output.png

│ └── logs.png

└── README.md

---

# Input

The system receives server health information through a JSON file.

Example:

```json
{
    "Server_A": "Healthy",
    "Server_B": "Down",
    "Server_C": "Healthy",
    "Server_D": "Down",
    "Server_E": "Healthy"
}
```

---

# Processing

The program performs the following steps:

1. Reads server status from JSON.
2. Checks each server's health.
3. Identifies healthy servers.
4. Removes unhealthy servers from routing.
5. Applies Round Robin scheduling.
6. Routes requests among healthy servers.
7. Generates logs.
8. Saves output to a JSON file.

---

# Output

Output JSON:

```json
{
    "healthy_servers": [
        "Server_A",
        "Server_C",
        "Server_E"
    ]
}
```

---

# Round Robin Scheduling

Round Robin is a simple and widely used load balancing algorithm.

Instead of sending all requests to a single server, requests are distributed sequentially among healthy servers.

Example:

Healthy Servers:

Server_A

Server_C

Server_E

Request Distribution:

Request 1 → Server_A

Request 2 → Server_C

Request 3 → Server_E

Request 4 → Server_A

Request 5 → Server_C

Request 6 → Server_E

This ensures equal workload distribution across all available servers.

---

# Features

* Health Check Monitoring
* Failure Detection
* Fault Tolerant Routing
* Round Robin Scheduling
* JSON Input and Output
* Logging Support
* Scalable Design
* Simple Implementation

---

# Technologies Used

* Python 3
* JSON
* Logging Module
* OS Module

---

# Log Generation

The system creates a log file named:

health_check.log

Example:

```text
2026-06-24 10:05:12 - INFO - Server_A is HEALTHY
2026-06-24 10:05:12 - WARNING - Server_B is DOWN
2026-06-24 10:05:12 - INFO - Request routed to Server_A
```

Logs help administrators monitor server status and routing decisions.

---

# How to Run

## Step 1

Clone the repository

```bash
git clone <repository-url>
```

## Step 2

Move to project directory

```bash
cd health_check_routing
```

## Step 3

Run the application

```bash
python health.py
```

---

# Sample Output

```text
===== HEALTH CHECK ROUTING SYSTEM =====

Healthy Servers:
['Server_A', 'Server_C', 'Server_E']

Routing Requests:

Request 1 --> Server_A
Request 2 --> Server_C
Request 3 --> Server_E
Request 4 --> Server_A
Request 5 --> Server_C
Request 6 --> Server_E
Request 7 --> Server_A
Request 8 --> Server_C
Request 9 --> Server_E
Request 10 --> Server_A
```

---

# Acceptance Criteria

✔ Failed servers must not receive requests

✔ Healthy servers should receive traffic

✔ Health check logs must be generated

✔ JSON output must be generated

✔ Round Robin load balancing must be implemented

---

# Advantages

* Improves reliability
* Enhances fault tolerance
* Reduces downtime
* Improves resource utilization
* Ensures equal load distribution
* Easy to monitor and maintain

---

# Real World Applications

* Cloud Infrastructure
* Data Centers
* Kubernetes Clusters
* Web Applications
* API Gateways
* NGINX Load Balancers
* HAProxy Load Balancers
* Microservices Architecture

---

# Future Enhancements

* Real-time server ping monitoring
* Weighted Round Robin
* Dynamic server registration
* Dashboard for server monitoring
* Email alerts for server failures
* Integration with cloud platforms

---

# Conclusion

The Health Check Based Routing System demonstrates how modern load balancers identify healthy servers and prevent traffic from being routed to failed machines.

The project combines health monitoring, failure detection, fault tolerance, and Round Robin scheduling to ensure reliable and efficient request handling.

By routing requests only to healthy servers, the system improves availability, reliability, and overall performance of distributed applications.
