import time

class Loop:
    
    def __init__(self, running, ps):
        self.running = running
        self.ps = ps

    def _set_running(self, running):
        self.running = running

    def _read_sensor(self, distance_sensor):

        from alerts.alert_service import AlertService
        while self.running:
            ret_val = distance_sensor.dummy_read_value()
            if int(ret_val["distance"]) < int(AlertService.treshhold):
                self.ps.pub("distance-sensor/alarm", ret_val)
            self.ps.pub("distance-sensor/data", ret_val)
            self.ps.pub("csv-writer/data", ret_val)
            #TODO Where to cleanup GPIO, is del sufficent?
            print("In read sensor loop")
            time.sleep(1.0)

