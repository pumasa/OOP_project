import socket
import pickle
import time


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 8000
        self.addr = (self.server, self.port)
        self.p = self.connect()
        # self.p = pickle.loads(self.p)

    def connect(self):
        self.client.connect(self.addr)
        return pickle.loads(self.client.recv(4096*8))

    def disconnect(self):
        self.client.close()

    def send(self, data, pick=False):
        start_time = time.time()

        while time.time() - start_time < 5:
            try:
                # if pick:
                self.client.send(pickle.dumps(data))
                # else:
                #     self.client.send(str.encode(data))
                reply = self.client.recv(4096*8)
                try:
                    reply = pickle.loads(reply)
                    break
                except Exception as e:
                    print(e)

            except socket.error as e:
                print(e)
        return reply

    def getP(self):
        return self.p
