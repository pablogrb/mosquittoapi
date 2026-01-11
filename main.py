"""
A FastAPI application that serves MQTT $SYS topics.

It uses a background thread to subscribe to MQTT $SYS topics and store the latest messages in a
dictionary. The API provides endpoints to retrieve all $SYS topics or a specific topic's value.
"""

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from mqtt_sys import data

app = FastAPI()

# Serve static files (dashboard and assets)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/dashboard")
def dashboard():
    """
    Serve the dashboard HTML page.
    """
    return FileResponse("static/dashboard.html")

@app.get("/sys")
def get_all_sys():
    """
    Get all stored $SYS topics and their latest values.
    """
    return data

@app.get("/sys/{topic:path}")
def get_sys_topic(topic: str):
    """
    Get the latest value for a specific $SYS topic.
    """
    key = f"$SYS/{topic}" if not topic.startswith("$SYS/") else topic
    if key in data:
        return {key: data[key]}
    return {"error": "Topic not found"}
