import time
import json
import random
import datetime
#import RPi.GPIO as GPIO
from config.config import Config
from alerts.alert_service import AlertService  
import threading

class DistanceSensor:

    #  Initialisierung
    def __init__(self, running, ps, sensorId_attr='KY-050'):
        self.sensorId = sensorId_attr
        self.triggerPin = 17
        self.echoPin = 27
        self.ps = ps
        '''
        GPIO.setup(TriggerPIN, GPIO.OUT)
        GPIO.setup(EchoPIN, GPIO.IN)
        GPIO.output(TriggerPIN, False)
        '''
        threading.Thread(target=self._read_sensor, args=(running, ps)).start()

    def __del__(self):
        '''
        GPIO.cleanup()
        '''
        print("Log del was called, GPIO was cleaned")

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
        
    '''    
    def read_value (self):
        GPIO.output(TriggerPIN, True)
        time.sleep(0.1)
        GPIO.output(TriggerPIN, False)

        timer1 = time.time()
        while GPIO.input(EchoPIN) == 0:
            timer1 = time.time()

        while GPIO.input(EchoPIN) == 1:
            timer2 = time.time()

        duration = timer2 - timer1
        distance = (duration * 34300) / 2

        distance = format((duration * 34300) / 2, '0.2f')
        return {
                "sensorId": self.sensorId,
                "timestamp": datetime.datetime \
                .fromtimestamp(time.time()).isoformat(),
                "distance": distance,
                "unit": "cm"
                }
    '''

    def _read_sensor(self, running, ps):
        while running:
            ret_val = self.dummy_read_value()
            if ret_val["distance"] < int(AlertService.treshhold):
                self.ps.pub("distance-sensor/alarm", json.dumps(ret_val))
            self.ps.pub("distance-sensor/data", json.dumps(ret_val))
            self.ps.pub("csv-writer/data", json.dumps(ret_val))
            #TODO Where to cleanup GPIO, is del sufficent?
            print("In read sensor loop")
            time.sleep(1.0)

