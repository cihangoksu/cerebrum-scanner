import socket
import os

from lib import server
clSERVER = server.Server()

def main():
    # Initializing the server
    clSERVER.init_server()
    clSERVER.accept_client()







if __name__ == "__main__":
    main()
