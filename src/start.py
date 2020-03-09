import time 
# Start der Anwendung

if __name__ == "__main__":
    from config.config import Config
    config = Config()

    from sensor.distance_sensor import DistanceSensor
    from utils.mqtt import MqttHandler
    from utils.pubsub import PubSubBroker

    ps = PubSubBroker()

    running = True 

    handlers = [
        DistanceSensor(running, ps),
        MqttHandler(ps)
        ]

    try:
        while True:
            time.sleep(10) 

    except KeyboardInterrupt:
        for handler in handlers:
            if hasattr(handler, "close"):
                handler.close()
        print("\nKeyboardInterupt")
