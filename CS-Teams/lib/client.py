# server-class
from __future__ import print_function, division

import sys
import os
head, tail = os.path.split(os.path.join(os.path.abspath(__file__)))

import socket

class Client(object):
    def __init__(self):
        super(Client, self).__init__()

        from _global_paths import __path_dict__
        self.__path_dict__ = __path_dict__
        self.host_ip = "192.168.1.106"
        # self.host_ip = "127.0.0.1"
        self.port = 44123
        self.server_socket = None
        self.client_socket = socket.socket()

    def connect_server(self):  
        print('Connecting the server...')
        self.client_socket.connect((self.host_ip, self.port))
        print("\n Client is connecting to server on port :", self.port, "\n")





    def send_msg(self, msg):
        # Send a message to server
        msg = f"{msg}"    
        self.client_socket.send(msg.encode())
        print(f"{msg} is now sent to server.")




    def send_file(self, file_path):
        # file_path = os.path.join(self.__path_dict__['dot-cerebrum-scanner-data'], 'CQ500-CT-0.zip')

        file = open(file_path, "rb")
        SendData = file.read(1024)

        while SendData:
            self.client_socket.send(SendData)
            SendData = file.read(1024)      

        # Close the connection from client side
        # self.close_socket()









    def receive_file(self):
        # Now we can receive data from server
        print("\n\n################## Below message is received from server ################## \n\n ", self.client_socket.recv(1024).decode("utf-8"))

        pass

    def close_socket(self):  
        # Close connection with client
        self.client_socket.close() 
        print("\n Connection is closed from the Client side!\n")
        self.client_socket_status = False











