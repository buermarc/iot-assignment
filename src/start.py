import time 
import threading
# Start der Anwendung

def _read_sensor(distance_sensor, ps):
    from alerts.alert_service import AlertService
    while distance_sensor.running:
        ret_val = distance_sensor.dummy_read_value()
        if int(ret_val["distance"]) < int(AlertService.treshhold):
            ps.pub("distance-sensor/alarm", ret_val)
        ps.pub("distance-sensor/data", ret_val)
        ps.pub("csv-writer/data", ret_val)
        #TODO Where to cleanup GPIO, is del sufficent?
        print("In read sensor loop")
        time.sleep(1.0)

if __name__ == "__main__":
    from config.config import Config
    from dhbw_iot_csv.csv_writer import CsvWriter
    config = Config()
    fieldnames = ['sensorId', 'timestamp', 'distance', 'unit']
    csv_writer = CsvWriter(fieldnames)

    from sensor.distance_sensor import DistanceSensor
    from utils.mqtt import MqttHandler
    from utils.pubsub import PubSubBroker

    ps = PubSubBroker()

    running = True 

    handlers = [
        DistanceSensor(running, ps),
        MqttHandler(ps)
        ]

    threading.Thread(target=_read_sensor, name="iot-sensor", args=(handlers[0], ps)).start()

    #Check for Exception TODO check immediately after initializing MqttHandler 
    if handlers[1].exception: 
        handlers[0].running = False
        raise Exception("Exception while connecting to MQTT Server and Topics")

    try:
        while True:
            time.sleep(10) 

    except KeyboardInterrupt:
        handlers[0].running = False #TODO get rid of '[0]'
        for handler in handlers:
            if hasattr(handler, "close"):
                handler.close()
                del handler
        print("\nKeyboardInterrupt in Main Loop")

        del config
        del csv_writer
