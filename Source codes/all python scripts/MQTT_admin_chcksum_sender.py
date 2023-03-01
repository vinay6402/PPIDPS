my_dict = {"boot.py": "3cdbd99c214a4ce83e2e5f089850b5c267ba54451", "connectwifi.py": "e0d4670a7b1cb2bb3cac749761004a956e62a493", "decision_tree_model.mpy": "84358e206a266346f31d194787d3ff3ecee6526b"}


import paho.mqtt.client as mqtt
import json
# Define the MQTT broker and topic
broker_address = "localhost"
topic = "chksum"

# Convert the dictionary to a JSON string
payload = json.dumps(my_dict)

# Define the callback function that will be called when the message is published
def on_publish(client, userdata, mid):
    print("Message published successfully")

# Set up the MQTT client
client = mqtt.Client()
client.on_publish = on_publish
client.connect(broker_address)

# Publish the message
result = client.publish(topic, payload)

# Check the result of the message publication
if result.rc == mqtt.MQTT_ERR_SUCCESS:
    print("Message sent successfully")
else:
    print("Message sending failed")
