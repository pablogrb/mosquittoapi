# Mosquitto $SYS REST API

This project provides a REST API to access the latest $SYS messages from a Mosquitto MQTT broker.

## Features
- Subscribes to all `$SYS/#` topics from a Mosquitto broker
- Stores the latest value for each sys topic in memory
- REST endpoints to fetch all or individual sys messages

## Requirements
- Python 3.13
- Mosquitto MQTT broker running and accessible (default: localhost:1883)

## Setup
1. Create and activate the virtual environment:
   ```sh
   python3.13 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set required environment variables:
   - `MQTT_BROKER_HOST`: The hostname or IP address of your Mosquitto broker (default: `localhost`)
   - `MQTT_BROKER_PORT`: The port number for your Mosquitto broker (default: `1883`)
   
   Example:
   ```sh
   export MQTT_BROKER_HOST=localhost
   export MQTT_BROKER_PORT=1883
   ```
4. Start the API server:
   ```sh
   uvicorn main:app --reload
   ```

## API Endpoints
- `GET /sys` — Get all latest $SYS messages
- `GET /sys/{topic}` — Get the latest value for a specific $SYS topic (omit the `$SYS/` prefix in the path)

## Dashboard Access

Once the API server is running, you can access the live MQTT stats dashboard in your browser:

- Open: [http://localhost:8000/dashboard.html](http://localhost:8000/dashboard.html)

The dashboard displays time series plots for clients, messages, and bytes.

If you are running the server on a different host or port, adjust the URL accordingly.

## Notes
- The API stores messages in memory only (no persistence).
- The MQTT broker address can be changed in `mqtt_sys.py` if needed.
