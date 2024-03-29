# server-class
from __future__ import print_function, division

import sys
import os
head, tail = os.path.split(os.path.join(os.path.abspath(__file__)))

import socket

import zipfile

class Server(object):
    def __init__(self):
        super(Server, self).__init__()

        from _paths import __path_dict__
        self.__path_dict__ = __path_dict__
        self.host_ip = "192.168.1.106"
        # self.host_ip = "127.0.0.1"
        self.port = 44123
        self.server_socket = None
        self.client_socket = None

        
    def init_server(self):  
        # Data augmentation and normalization for training
        print('Initializing the server...')

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host_ip, self.port))  # Change IP and port as needed
        self.server_socket.listen(1) # number of allowed listening clients! This should be changed to many in the future


        print("\n Server is listing on port :", self.port, "\n")


    def accept_client(self):  
        
        while True:
            self.client_socket, addr = self.server_socket.accept()
            print("Client connected")

            # Receive message from the client
            msg = self.receive_msg()
            self.apply_command(msg)


    def receive_msg(self):
        # Now we can receive data from server
        msg = self.client_socket.recv(1024).decode("utf-8")
        print(f'msg is received from the client: {msg}')
        return msg


    def apply_command(self, msg):
        print('applying the command now')
        msg_list = msg.split(':')
        if msg_list[0] != 'command': 
            print(f"No command is sent: {msg}")
            return None
        cmd = msg_list[1]
        print('cmd is' + cmd)
        if cmd == 'receive_case': 
            print('receiving the file...')
            receive_out = self.receive_file()
            print(f"Applied command is: {cmd}")
            print(receive_out)
            
            self.extract_zip_in_tmp()
            print(f"Case is now in the server received-folders")

        else: return None


        # Now we can receive data from server
        
        
        
        
        return None


    ##########################################
    ##########################################
    def receive_file(self):
        #Open one recv.txt file in write mode
        received_zip_file_path = os.path.join(self.__path_dict__['dot-cerebrum-scanner-tmp'],'received.zip')

        print('file path is:' + received_zip_file_path)

        with open(received_zip_file_path, "wb") as file:
            print('inside with open')
            iter_num = 0
            while True:
                iter_num += 1
                print(f'iter #{iter_num}')
                data = self.client_socket.recv(1024)
                print(type(data))
                if data: 
                    print('writing...')
                    file.write(data)
                else:
                    print('Loop is now broken')
                    break


                
                    
        print("\n File has been copied successfully \n")



    def extract_zip_in_tmp(self):
        received_zip_file_path = os.path.join(self.__path_dict__['dot-cerebrum-scanner-tmp'],'received.zip')
        dest_path = os.path.join(self.__path_dict__['dot-cerebrum-scanner-jobs'],'received')

        import shutil
        shutil.unpack_archive(received_zip_file_path, dest_path)
        


    def send_file(filename, client_socket):
        try:
            with open(filename, "rb") as file:
                file_data = file.read()
                client_socket.sendall(file_data)
        except Exception as e:
            print("Error sending file:", e)


    # filename = "example.txt"  # Change to the desired file name
    # send_file(filename, client_socket)

    ##########################################
    ##########################################

    def close_socket(self):  
        # Close connection with client
        self.client_socket.close() 
        print("\n Server closed the connection \n")





