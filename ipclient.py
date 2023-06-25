import socket
from pickle import dumps as encode
from pickle import loads as decode

class IpClient:
    def __init__(self, host, port):
        self.connection = (host, port)
    
    # send a request message and returns the server response
    def request(self, message):
        client_socket = socket.socket()  # instantiate
        client_socket.settimeout(3)
        client_socket.connect(self.connection)  # connect to the server

        client_socket.send(encode(message))  # send message
        data = None
        try:
            data = decode(client_socket.recv(1024))  # receive response
        except:
            pass

        client_socket.close()  # close the connection

        return data
