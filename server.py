import socket
from _thread import start_new_thread
import sys

server = "localhost"
port = 8000

# AF_INET is for IPv4 address, SOCK_STREAM is how the info is handled
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.error as e:
    str(e)
# Listen for connections (4 is the number of connections allowed)
s.listen(4)
print("Waiting for connections, Server started")


def threaded_client(conn):

    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Recieved: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))

        except:
            break

    print("Lost connection")
    conn.close()


while True:
    # Will accept any incoming connections
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))
