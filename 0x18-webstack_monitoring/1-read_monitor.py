#!/usr/bin/python3
from datadog import initialize, api

# Initialize the DataDog API client
options = {
    'api_key': '<3d79c9f38167c760c309afeeb4cd3320>',
    'app_key': '<3d79c9f38167c760c309afeeb4cd3320>'
}

initialize(**options)

# Define the monitor configuration for read requests
read_monitor = {
    "type": "metric alert",
    "query": "avg(last_1m):sum:system.disk.reads{host:host_name} by {device} > 100",
    "name": "Read Requests Per Second",
    "message": "Read requests per second on {device} are above threshold",
    "tags": ["device:device_name"],
    "options": {
        "notify_no_data": True,
        "no_data_timeframe": 10,
        "notify_audit": False,
        "locked": False,
        "timeout_h": 0,
        "silenced": {}
    }
}

# Define the monitor configuration for write requests
write_monitor = {
    "type": "metric alert",
    "query": "avg(last_1m):sum:system.disk.writes{host:host_name} by {device} > 100",
    "name": "Write Requests Per Second",
    "message": "Write requests per second on {device} are above threshold",
    "tags": ["device:device_name"],
    "options": {
        "notify_no_data": True,
        "no_data_timeframe": 10,
        "notify_audit": False,
        "locked": False,
        "timeout_h": 0,
        "silenced": {}
    }
}

# Create the monitors
api.Monitor.create(**read_monitor)
api.Monitor.create(**write_monitor)

print("Monitors created successfully.")

