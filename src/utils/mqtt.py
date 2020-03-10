import paho.mqtt.client as mqtt
from alerts.alert_service import AlertService
from data.dataservice import DataService
from config.config import Config
from csv.csv_writer import CsvWriter
class MqttHandler:
    client = None

    def __init__(self, ps):
        self.ps = ps
        self.ps.sub("distance-sensor/alarm", \
                AlertService.on_distance_threshold_passed)
        self.ps.sub("distance-sensor/data", DataService.send_data)
        self.ps.sub("csv-writer/write", CsvWriter.write_line) 
        self.ps.sub("config/treshhold", AlertService.set_alert_threshold)
        MqttHandler.client = mqtt.Client()
        MqttHandler.client.connect(Config.broker_host, Config.broker_port)
        MqttHandler.client.on_message = self.on_message
        MqttHandler.client.subscribe(Config.config_topic, qos=1)

        MqttHandler.client.loop_start()

    def on_message(self, client, userdata, message):
        if message.topic == Config.config_topic:
            self.ps.pub("config/treshhold", int(message.payload.decode()))

