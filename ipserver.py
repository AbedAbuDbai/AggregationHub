import socket
from pickle import dumps as encode
from pickle import loads as decode

class IpServer:
    def __init__(self, host, port):
        self.server_socket = socket.socket()  # get instance
        self.server_socket.settimeout(1)
        # look closely. The bind() function takes tuple as argument
        self.server_socket.bind((host, port))  # bind host address and port together
        # configure how many client the server can listen simultaneously
        self.server_socket.listen(1)

    # return the accepted request from client
    def accept(self):
        try:
            self.conn, address = self.server_socket.accept()  # accept new connection
        except:
            return dict()

        print("Connection from: " + str(address))
        
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = decode(self.conn.recv(1024))
        if not data:
            # if data is not received break
            self.conn.close()
            return dict()
        
        print("from connected user: " + str(data))
        return data

    # send the data as a response to the connected client    
    def response(self, data):
        self.conn.send(encode(data))  # send data to the client
        self.conn.close()  # close the connection
