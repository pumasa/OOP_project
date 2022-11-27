import socket
from _thread import start_new_thread
from Objects.player import Player
import pickle
import pygame
import time

server = "localhost"
port = 8000

# AF_INET is for IPv4 address, SOCK_STREAM is how the info is handled
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)
    quit()

# Listen for connections (2 is the number of connections allowed)
s.listen()
print("Waiting for a connection, Server Started")


connections = 0


p1 = Player(32, 32, 29, 29)
p2 = Player(736, 448, 29, 29)

players = [p1, p2]


def threaded_client(conn, player):
    global connections, currentID

    conn.send(pickle.dumps(players[player]))
    reply = ""

    if connections % 2 == 0:
        currentID = "Y"
        print("Player 1 connected")
    else:
        currentID = "R"
        print("Player 2 connected")

    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                # print("Received: ", data)
                # print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except socket.error as e:
            print(e)
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0

while True:
    # Will accept any incoming connections
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
