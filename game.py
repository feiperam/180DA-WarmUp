import paho.mqtt.client as mqtt
import time

# Define MQTT broker details
broker_address = "mqtt.eclipse.org"
broker_port = 1883

# Define game state
players = ["Player 1", "Player 2", "Player 3"]
moves = {}
round_number = 1

def on_connect(client, userdata, flags, rc):
    print("Game server connected with result code " + str(rc))
    for player in players:
        client.subscribe(f"rps/{player}/move")

def on_message(client, userdata, msg):
    global moves
    player = msg.topic.split("/")[1]
    move = msg.payload.decode()
    print(f"{player} move: {move}")
    moves[player] = move

def display_results():
    global round_number
    print(f"\nRound {round_number} - Game Results:")
    for player in players:
        print(f"{player}: {moves.get(player, 'No move yet')}")
    round_number += 1

def play_game():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker_address, broker_port, 60)
    client.loop_start()

    print("Rock, Paper, Scissors Game - Multiplayer with Tabulated Results\n")

    while True:
        moves.clear()
        for player in players:
            time.sleep(1)  # Ensure a slight delay between player turns
            move = input(f"{player}, enter your move (rock, paper, scissors): ")
            client.publish(f"rps/{player}/move", move)

        time.sleep(1)  # Wait for results to be collected
        display_results()

if __name__ == "__main__":
    play_game()
