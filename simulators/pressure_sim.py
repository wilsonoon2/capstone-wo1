import time
import json
import random
import os
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# -----------------------------
# CONFIGURATION
# -----------------------------
CLIENT_ID = "PressureSensor-01"
TOPIC = "factory/sensors/pressure"

ENDPOINT = "a19iwwhi2w6u01-ats.iot.ap-southeast-1.amazonaws.com"

# -----------------------------
# Correct relative directory
# -----------------------------
CERT_DIR = "../certificates/pressure"

ROOT_CA_PATH = os.path.join(CERT_DIR, "AmazonRootCA1.pem")
PRIVATE_KEY_PATH = os.path.join(CERT_DIR, "pressurePrivateKey.pem")
CERT_PATH = os.path.join(CERT_DIR, "pressureCert.pem")

# -----------------------------
# MQTT CLIENT SETUP
# -----------------------------
client = AWSIoTMQTTClient(CLIENT_ID)
client.configureEndpoint(ENDPOINT, 8883)
client.configureCredentials(ROOT_CA_PATH, PRIVATE_KEY_PATH, CERT_PATH)

client.configureOfflinePublishQueueing(-1)
client.configureDrainingFrequency(2)
client.configureConnectDisconnectTimeout(10)
client.configureMQTTOperationTimeout(5)

client.connect()

print("Simulator started. Publishing to AWS IoT Core...")

# -----------------------------
# MAIN LOOP
# -----------------------------
while True:
    pressure_psi = round(random.uniform(35.0, 50.0), 2)
    pressure_kpa = round(pressure_psi * 6.89476, 2)
    now = time.time()  # double timestamp (your SiteWise model accepts double)

    payload = {
        "device_id": CLIENT_ID,
        "pressure_psi": pressure_psi,
        "pressure_kpa": pressure_kpa,
        "timestamp": now
    }

    client.publish(TOPIC, json.dumps(payload), 1)
    print("Published:", payload)
    time.sleep(2)

