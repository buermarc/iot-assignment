from config.config import Config
import json
#TODO fix imports

class AlertService: # Service Reagiert auf Messwerte
    #Static teshhold
    treshhold = 42
    #  Initialisierung und subs
    def __init__(self):
        pass

    #  value:  Neuer Schwellwert als einfache Zahl in der Einheit cm wird hier übergeben
    def set_alert_threshold(message):
        #TODO check if it is an int
        AlertService.treshhold = int(message);


    #  value:  Aktuell gemessener Wert (siehe DistanceSensor) wird übergeben und es wird ein Alarm gesendet
    def on_distance_threshold_passed(value):
        from utils.mqtt import MqttHandler as mqtt
        mqtt.client.publish(Config.alert_topic, json.dumps(value))
        # write to mqtt topic in config.json


