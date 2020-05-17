import time
import json
import random
import datetime
import RPi.GPIO as GPIO
import logging
from config.config import Config
from alerts.alert_service import AlertService  

log = logging.getLogger(__name__)

class DistanceSensor:

    #  Initialisierung
    def __init__(self, sensorId_attr='KY-050'):
        self.sensorId = sensorId_attr
        self.triggerPin = 17
        self.echoPin = 27
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.triggerPin, GPIO.OUT)
        GPIO.setup(self.echoPin, GPIO.IN)
        GPIO.output(self.triggerPin, False)

    def __del__(self):
        GPIO.cleanup()
        log.info("Log del was called, GPIO was cleaned")


    #  return Wert als Dictionary entsprechend folgendem JSON:
    #   { 
    #     "sensorId"  : "KY-050", 
    #     "timestamp" : "2020-03-01T12:00:01.345+01:00",
    #     "distance" : 42,
    #     "unit" : "cm"
    #   }
    def dummy_read_value(self): 
        return {
                "sensorId": self.sensorId,
                "timestamp": datetime.datetime \
                .fromtimestamp(time.time()).isoformat(),
                "distance": random.randrange(0,150,1),
                "unit": "cm"
                }
        
    def read_value (self):
        GPIO.output(self.triggerPin, True)
        time.sleep(0.1)
        GPIO.output(self.triggerPin, False)

        timer1 = time.time()
        while GPIO.input(self.echoPin) == 0:
            timer1 = time.time()

        while GPIO.input(self.echoPin) == 1:
            timer2 = time.time()

        duration = timer2 - timer1
        distance = (duration * 34300) / 2

        distance = format((duration * 34300) / 2, '0.0f')
        return {
                "sensorId": self.sensorId,
                "timestamp": datetime.datetime \
                .fromtimestamp(time.time()).isoformat(),
                "distance": distance,
                "unit": "cm"
                }

    '''
    def _read_sensor(self, dummy, ps):
        while self.running:
            ret_val = self.read_value()
            if int(ret_val["distance"]) < int(AlertService.treshhold):
                self.ps.pub("distance-sensor/alarm", ret_val)
            self.ps.pub("distance-sensor/data", ret_val)
            self.ps.pub("csv-writer/data", ret_val)
            #TODO Where to cleanup GPIO, is del sufficent?
            print("In read sensor loop")
            time.sleep(1.0)
    '''
