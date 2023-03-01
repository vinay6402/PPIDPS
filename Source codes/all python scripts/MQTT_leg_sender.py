import paho.mqtt.client as mqtt
import time
Leg_list = ["BPL-1G-58","RMI-3G-57","OPI-2G-22","stock", "database", "available", "temp: 30", "hum: 47"]
def on_connect(client, userdata, flags, rc):
    for leg in Leg_list:
        client.publish("iot_channel", leg)
        time.sleep(0.1)
    client.disconnect()

client = mqtt.Client()
client.on_connect = on_connect

client.connect("localhost", 1883, 60)

client.loop_forever()
