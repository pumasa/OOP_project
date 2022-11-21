import socket
from _thread import start_new_thread
from player import Player
import pickle

server = "localhost"
port = 8000

# AF_INET is for IPv4 address, SOCK_STREAM is how the info is handled
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# Listen for connections (2 is the number of connections allowed)
s.listen(2)
print("Waiting for a connection, Server Started")


players = [Player(0, 0, 50, 50, (255, 0, 0)), Player(100, 100, 50, 50, (0, 0, 255))]


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
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
                elif player == 2:
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
