# Health Check Based Routing System

## Objective

This project implements a Health Check Based Routing System
that routes requests only to healthy servers.

## Features

- Health Status Monitoring
- Failure Detection
- Request Routing
- Health Check Logging
- JSON Input and Output
- Fault Tolerant Design

## Input

{
    "Server_A":"Healthy",
    "Server_B":"Down",
    "Server_C":"Healthy"
}

## Output

{
    "healthy_servers":[
        "Server_A",
        "Server_C"
    ]
}

## Technologies Used

- Python 3
- JSON
- Logging Module

## How To Run

python health_check_router.py

## Acceptance Criteria

✔ Failed servers never receive requests

✔ Healthy servers receive traffic

✔ Health check logs generated

✔ JSON output generated