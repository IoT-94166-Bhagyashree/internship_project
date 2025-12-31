from flask import Flask
import paho.mqtt.client as mqtt
import requests
import json

app = Flask(__name__)

THINGSPEAK_API_KEY = "8ENFC82ABDK7400L"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "env/esp32/data"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    temp = data["temperature"]
    hum = data["humidity"]
    gas = data["gas"]

    payload = {
        "api_key": THINGSPEAK_API_KEY,
        "field1": temp,
        "field2": hum,
        "field3": gas
    }

    response = requests.get(THINGSPEAK_URL, params=payload)
    print("Sent to ThingSpeak:", response.text)

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.loop_start()

@app.route("/")
def home():
    return "Flask MQTT → ThingSpeak Server Running"

if __name__ == "__main__":
    app.run(debug=True)
