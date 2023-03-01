print("exeing main.py")
#importing libraries
from umqtt.simple import MQTTClient
from time import sleep
from decision_tree_model import score
import connectwifi
import urequests as requests
import ujson as json
from machine import RTC, reset,UART
from hashlib import sha1
from binascii import hexlify

uart = UART(2, baudrate=115200)
#-------------alert_logger----------
def alert_logger(topic, mal_msg):
    url = 'http://192.168.24.12:5000/append_csv'
    headers = {'Content-Type': 'application/json'}
    time = RTC().datetime()
    t1 = str(time[0]) + ":" + str(time[1]) + ":" + str(time[2]) + ":" + str(time[4]) + ":" + str(time[5]) + ":" + str(time[6])
    my_list = [["date_time: " + t1, "topic: " + topic.decode() , mal_msg]]
    payload = json.dumps({'my_list': my_list})
    response = requests.post(url, headers=headers, data=payload)
    #print(response.text)
#----------checksum-----------------
def hasher(file):
    sha = sha1()
    with open(file, 'rb') as f:
        while True:
            data = f.read(1024) # changed from 4096 to 1024
            if not data:
                break
            sha.update(data)
    return (hexlify(sha.digest()).decode('utf-8'))

#-serial data from esp to arduino---
def serial_cb(data):
    topic = "End_Node"
    unique_words = set()
    data = remove_python_symbols(data)
    words = get_words_from_code(data)
    unique_words.update(words)
    #print(unique_words)
    res = ML_pred(unique_words)
    if( res == "legit_data"):
        print(res)
        mqttc.publish("iot_channel", data)
    elif( res == "mal_data"):
        print(res)
        alert_logger(topic.encode(),(" ".join(unique_words)))
#-----------softwareupdate----------
def sw_updater(msg):
    print(msg)
    import ver_details as ver
    msglist = msg.decode().split(", ")
    if(ver.version < float(msglist[0])):
        print("new update is available and updating in process")
        url = "http://192.168.24.12:80/"
        for i in msglist[1:]:
            response = requests.get(url + str(float(msglist[0])) + "/" + i)
            print("attempting to download: " + i)
            with open(i, "w") as f:
                f.write(response.text)
        response.close()
        print("update completed & restarting machine")
        reset()
#-------------ML--------------------
def remove_python_symbols(code):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789- \t\n\r\f\v'
    code = ''.join(c if c in allowed_chars else ' ' for c in code)
    code = code.replace('_', ' ')
    code = ' '.join(code.split())
    gc.collect()
    return code

def get_words_from_code(code):
    # split the code into words
    words = code.split(' ')
    words = [x for x in words if len(x) > 1]
    gc.collect()
    return words

def ML_pred(words_list):
    b = []
    for word in words_list:
        a = [ord(x.upper()) for x in word]
        a = a + [0] * (25 - len(a))
        prediction = score(a)
        b.append(prediction.index(max(prediction)))
        gc.collect()
        if ( len(b) ==3):
            return "mal_data"
    return "legit_data"
#---------------mqtt---------------------
def sub_cb(topic, msg):
    if(topic == b'iot_channel'):
        code = msg.decode()
        unique_words = set()
        code = remove_python_symbols(code)
        words = get_words_from_code(code)
        unique_words.update(words)
        #print(unique_words)
        res = ML_pred(unique_words)
        if( res == "legit_data"):
            print(res)
            uart.write(msg)
        elif( res == "mal_data"):
            print(res)
            alert_logger(topic,(" ".join(unique_words)))
    if (topic == b'sw_update'):
        sw_updater(msg)
    if (topic == b'chksum'):
        my_dict = json.loads(msg)
        NotMatch = []
        for key, value in my_dict.items():
            if not(hasher(key) == value):
                NotMatch.append(key)
        print(NotMatch)
        pub_msg = (connectwifi.sta_if.ifconfig()[0] + ' is having missmatching checksum in files: ' + (','.join(NotMatch))).encode('utf-8')
        print(pub_msg)
        mqttc.publish("chksum_missmatch", pub_msg)

#mqtt setup
client_id = 'espclient'
server_ip = '192.168.24.12'
topic_sub = b'iot_channel'
topic_pub = b'hello'
mqttc = MQTTClient(client_id, server_ip, keepalive=600)
mqttc.set_callback(sub_cb)
a = mqttc.connect()
if (a==0):
    print("Connected to MQTT server")
else:
    print("Can not connect to MQTT server")
mqttc.subscribe(topic_sub)
mqttc.subscribe(b'sw_update')
mqttc.subscribe(b'chksum')
#-----------------------------------------
#loop
while True:
    mqttc.check_msg()
    gc.collect()
    if uart.any():
        data = str(uart.read())
        serial_cb(data)
    sleep(1)
