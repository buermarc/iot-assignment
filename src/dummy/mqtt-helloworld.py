import paho.mqtt.client as mqtt

broker_url = "iot.eclipse.org"
broker_port = 1883

client = mqtt.Client()
client.connect(broker_url, broker_port)

def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code " (rc))

def on_message_from_kitchen(client, userdata, message):
    print("Message Recived from Kitchen: " + message.payload.decode())


