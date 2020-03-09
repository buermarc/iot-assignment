from config.config import Config

class DataService:

    def send_data(message): 
        from utils.mqtt import MqttHandler as mqtt
        mqtt.client.publish(Config.data_topic, message)
