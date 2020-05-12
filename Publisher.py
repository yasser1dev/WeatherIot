import json
import random
import threading
from datetime import datetime
import paho.mqtt.client as mqtt

MQTT_BROKER="mqtt.eclipse.org"
MQTT_Topic_Humidity = "Home/BedRoom/DHT1/Humidity"
MQTT_Topic_Temperature = "Home/BedRoom/DHT1/Temperature"
MQTT_Topic_Acceleration = "Home/BedRoom/DHT1/Acceleration"
MQTT_Port = 1883
Keep_Alive_Interval = 30
def on_connect(client,userdata,rc):
    if rc !=0:
        pass
        print("Unable to connect to broker")
    else :
        print("Connected with MQTT Broker :"+str(MQTT_BROKER))

def on_publish(client,userdata,mid):
    pass

def on_disconnect(client,userdata,rc):
    if rc!=0:
        pass

def publishToTopic(topic,message):
    mqttc.publish(topic,message)
    print("Publish message : "+str(message)+ " to topic : "+str(topic))
    print("")

def getHumidityLevel(humidityValue):
    if humidityValue<=30:
        return 'LOW'
    elif humidityValue<=60:
        return 'Medium'
    else: return 'high'

def getTempLevel(TmpVelue):
    if TmpVelue<=5:
        return 'very cold'
    elif TmpVelue<=15:
        return 'cold'
    elif TmpVelue<=25:
        return 'normal'
    elif TmpVelue<=30:
        return 'hot'
    else : return "very hot"

def getRandomNumber():
    m=float(10)
    s_rm=1-(1/m)**2
    return (1-random.uniform(0,s_rm))**.5

def publishDataToMqtt():
    threading.Timer(2.0,publishDataToMqtt).start()
    global toggle
    if toggle==0 :
        humidityValue=float("{0:.2f}".format(random.uniform(10,100)*getRandomNumber()))
        humidityData={}
        humidityData['SensorId']="humidity-sensor1"
        humidityData['Date']=(datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
        humidityData['HumidityLevel']=getHumidityLevel(humidityValue)
        humidityJsonData=json.dumps(humidityData)
        print("Publish humidity data"+ str(humidityData))
        publishToTopic(MQTT_Topic_Humidity,humidityJsonData)
        toggle=1
    else :
        #temperature
        tmpValue = float("{0:.2f}".format(random.uniform(-5, 45) * getRandomNumber()))
        tmpData = {}
        tmpData['SensorId'] = "Temeperature-sensor1"
        tmpData['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
        tmpData['HumidityLevel'] = getHumidityLevel(tmpValue)
        tmpJsonData = json.dumps(tmpData)
        print("Publish humidity data" + str(tmpData))
        publishToTopic(MQTT_Topic_Humidity, tmpJsonData)
        toggle=0






mqttc=mqtt.Client()
mqttc.on_connect=on_connect
mqttc.on_disconnect=on_disconnect
mqttc.on_publish=on_publish
mqttc.connect(MQTT_BROKER,int(MQTT_Port),int(Keep_Alive_Interval))
toggle=0
publishDataToMqtt()
