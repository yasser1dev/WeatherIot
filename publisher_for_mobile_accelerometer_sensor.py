import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime
from time import sleep
import re
from pynput import keyboard
import socket, traceback
import time

def on_press(key):
    global break_program
    print (key)
    if key == keyboard.Key.end:
        print ('end pressed')
        break_program = True
        return False

def mapMsgToJson(msg,addr):
    dic = {}
    lst = re.split("[,\"]",str(msg))
    dic['sensor_id'] = 'Accelerometer '+str(addr)
    dic['date_time'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
    dic['accX'] = lst[3].strip()
    dic['accY'] = lst[4].strip()
    dic['accA'] = lst[5].strip()
    return json.dumps(dic)

def on_connect(client, userdata ,rc):
    if rc != 0:
        pass
        print("Unable to connect to MQTT Broker...")
    else:
        print("Connected with MQTT Broker: "+str(MQTT_Broker))

def on_publish(client, userdata, mid):
    pass

def on_disconnect(client, userdata, rc):
    if rc != 0:
        pass

def publish_to_topic(topic, message):
    mqttc.publish(topic, message)
    print("Published: "+str(message)+" on MQTT Topic: "+str(topic))
    print("")

#MQTT Settings
MQTT_Broker = "mqtt.eclipse.org"
MQTT_Port = 1883
Keep_alive_interval = 30
MQTT_topic_acceleration = "Home/BedRoom/DHT1/Acceleration"

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_alive_interval))

break_program = False
host = '192.168.0.102'
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

with keyboard.Listener(on_press = on_press) as listener:
    while break_program == False:
        try:
            message, address = s.recvfrom(8192)
            acceleration_json_data = mapMsgToJson(message, address)
            publish_to_topic(MQTT_topic_acceleration, acceleration_json_data)
            sleep(1) #make a pause
        except:
            traceback.print_exc();
    listener.join()