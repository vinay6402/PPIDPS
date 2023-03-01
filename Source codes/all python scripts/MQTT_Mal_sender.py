import paho.mqtt.client as mqtt
import os
import glob
import time
folder_path = "CodeCleaner/CodesDir"
def on_connect(client, userdata, flags, rc):
    for filename in glob.glob(os.path.join(folder_path, "*")):
        if os.path.isfile(filename):
            with open(filename) as file:
                file_contents = file.read()
            client.publish("iot_channel", file_contents)
            time.sleep(0.1)
    client.disconnect()

client = mqtt.Client()
client.on_connect = on_connect

client.connect("localhost", 1883, 60)

client.loop_forever()
