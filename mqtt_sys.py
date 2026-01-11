"""
A module that subscribes to MQTT $SYS topics and stores the latest messages in a dictionary.
"""
import threading
import os
import paho.mqtt.client as mqtt

# Dictionary to store latest sys messages
data = {}


MQTT_BROKER_HOST = os.getenv("MQTT_BROKER_HOST", "localhost")
MQTT_BROKER_PORT = int(os.getenv("MQTT_BROKER_PORT", "1883"))

def on_connect(client, userdata, flags, rc):
    """
    The callback for when the client receives a CONNACK response from the server.
    """
    # discard the unused parameters
    _ = userdata
    _ = flags
    _ = rc
    client.subscribe("$SYS/#")

def on_message(client, userdata, msg):
    """
    The callback for when a PUBLISH message is received from the server.
    """
    # discard the unused parameters
    _ = client
    _ = userdata
    data[msg.topic] = msg.payload.decode()


def start_mqtt():
    """
    Start the MQTT client and subscribe to $SYS topics.
    """
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)
    client.loop_forever()

mqtt_thread = threading.Thread(target=start_mqtt, daemon=True)
mqtt_thread.start()
