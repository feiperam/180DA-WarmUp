import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"{userdata} connected with result code {rc}")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

player_name = input("Enter your player name: ")
client = mqtt.Client(userdata=player_name)
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)
client.subscribe(f"rps/{player_name}/move")

client.loop_forever()
