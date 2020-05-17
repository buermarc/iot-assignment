import sys
import time 
import threading
import logging
# Start der Anwendung

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    if int(sys.version[0]) != 3:
        log.error("Please run with Python 3")
        exit(1)


    from config.config import Config
    from dhbw_iot_csv.csv_writer import CsvWriter

    config = Config()
    fieldnames = ['sensorId', 'timestamp', 'distance', 'unit']
    csv_writer = CsvWriter(fieldnames)

    from sensor.distance_sensor import DistanceSensor
    from utils.mqtt import MqttHandler
    from utils.pubsub import PubSubBroker
    from utils.loop import Loop

    ps = PubSubBroker()

    running = True
    handlers = [
        DistanceSensor(),
        MqttHandler(ps),
        Loop(running, ps)
        ]

    threading.Thread(target=handlers[2]._read_sensor, name="iot-sensor", args=([handlers[0]])).start()

    #Check for Exception TODO check immediately after initializing MqttHandler 
    if handlers[1].exception: 
        loop._set_running(False)
        raise Exception("Exception while connecting to MQTT Server and Topics")

    try:
        while True:
            time.sleep(10) 

    except KeyboardInterrupt:
        handlers[2]._set_running(False)
        for handler in handlers:
            if hasattr(handler, "close"):
                handler.close()
                del handler
        log.info("KeyboardInterrupt in Main Loop")

        del config
        del csv_writer
