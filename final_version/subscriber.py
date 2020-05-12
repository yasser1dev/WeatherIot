import paho.mqtt.client as mqtt
from storeData import sensor_Data_Handler

def on_connect(mosq, obj, rc):
    if rc == 0:
        print("Connected")
        mqttc.subscribe(MQTT_Topic, 0) # Subscribe to all sensors at Base Topic
    else:
        print("Bad Connection")

def on_message(mosq, obj, msg):
    #this is the Master call for saving MQTT Date into DB
    print("MQTT Data Received ...")
    print("MQTT Topic: "+ msg.topic)
    print("Data: "+str(msg.payload))
    sensor_Data_Handler(msg.topic, msg.payload) #Save Data into DB Table

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

#MQTT Settings
MQTT_Broker = "mqtt.eclipse.org"
MQTT_Port = 1883
Keep_alive_interval = 30
MQTT_Topic = "Home/BedRoom/#"
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect & Subscribe
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_alive_interval))
mqttc.subscribe((MQTT_Topic, 0))

mqttc.loop_forever() #Continue the network loop