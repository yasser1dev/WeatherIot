import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime

def on_connect(client, userdata, rc):
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

# Code used as simulated sensor to publish some random values to MQTT Broker
def getHumidityLevel(humidityValue):
    if humidityValue <= 30:
        return 'LOW'
    elif humidityValue <= 60:
        return 'MEDUIM'
    else:
        return 'HIGH'

def getTemperatureLevel(temeratureValue):
    if temeratureValue <= 5:
        return 'VERY COLD'
    elif temeratureValue <= 15:
        return 'COLD'
    elif temeratureValue <= 25:
        return 'NORMAL'
    elif temeratureValue <= 35:
        return 'HOT'
    else:
        return 'VERY HOT'

def getRandomNumber():
    m = float(10)
    s_rm = 1-(1/m)**2
    return (1-random.uniform(0, s_rm))**.5

def publish_sensor_values_to_mqtt():
    threading.Timer(2.0, publish_sensor_values_to_mqtt).start()
    global toggle
    if toggle == 0:
        humidityValue = float("{0:.2f}".format(random.uniform(10,100)*getRandomNumber()))
        humidityData = {}
        humidityData['sensor_id'] = "Humidity-Sensor1"
        humidityData['date_time'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
        humidityData['humidity'] = humidityValue
        humidityData['humidity_level'] = getHumidityLevel(humidityValue)
        humidity_json_data = json.dumps(humidityData)
        print("Publishing humidity values : "+str(humidityValue)+" ...")
        publish_to_topic(MQTT_topic_humidity, humidity_json_data)
        toggle = 1
    else:
        temperatureValue = float("{0:.2f}".format(random.uniform(-5, 45) * getRandomNumber()))
        temperatureData = {}
        temperatureData['sensor_id'] = "Temperature-sensor1"
        temperatureData['date_time'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
        temperatureData['temperature'] = temperatureValue
        temperatureData['temperature_level'] = getTemperatureLevel(temperatureValue)
        temperature_json_data = json.dumps(temperatureData)
        print("Publishing Temperature values" + str(temperatureData)+" ...")
        publish_to_topic(MQTT_topic_temperature, temperature_json_data)
        toggle = 0

#MQTT Settings
MQTT_Broker = "mqtt.eclipse.org"
MQTT_Port = 1883
Keep_alive_interval = 30
MQTT_topic_humidity = "Home/BedRoom/DHT1/Humidity"
MQTT_topic_temperature = "Home/BedRoom/DHT1/Temperature"

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_alive_interval))
toggle = 0
publish_sensor_values_to_mqtt()