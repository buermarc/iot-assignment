import time 
# Start der Anwendung

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

    #Check for Exception TODO check immediately after initializing MqttHandler 
    if handlers[1].exception: 
        handlers[0].set_running(False)
        raise Exception("Exception while connecting to MQTT Server and Topics")

    try:
        while True:
            time.sleep(10) 

    except KeyboardInterrupt:
        handlers[0].set_running(False) #TODO get rid of '[0]'
        for handler in handlers:
            if hasattr(handler, "close"):
                handler.close()
                del handler
        print("\nKeyboardInterrupt in Main Loop")

        del config
        del csv_writer
