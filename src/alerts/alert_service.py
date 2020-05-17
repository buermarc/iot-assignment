from config.config import Config
import json
import logging
log = logging.getLogger(__name__)
#TODO fix imports

class AlertService: # Service Reagiert auf Messwerte
    #Static teshhold
    treshhold = 42
    #  Initialisierung und subs
    def __init__(self):
        pass

    #  value:  Neuer Schwellwert als einfache Zahl in der Einheit cm wird hier uebergeben
    def set_alert_threshold(message):
        #TODO check if it is an in, at the moment thread throws Exception but we don't care
        #Set treshhold if it is < 300

        try:
            message = int(message)
        except Exception:
            log.warn("Message received  in 'distance-sensor/config' can not be cast to type int")
            return 

        AlertService.treshhold = min(300,message)
        log.info("New treshhold is: %s", AlertService.treshhold)




    #  value:  Aktuell gemessener Wert (siehe DistanceSensor) wird uebergeben und es wird ein Alarm gesendet
    def on_distance_threshold_passed(value):
        from utils.mqtt import MqttHandler as mqtt
        mqtt.client.publish(Config.alert_topic, json.dumps(value))
        log.info("Alarm treshhold was passed. Alarm was published")
        # write to mqtt topic in config.json


