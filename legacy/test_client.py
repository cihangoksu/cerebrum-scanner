from lib import client
clCLIENT = client.Client()


def main():
    # Initializing the server
    clCLIENT.connect_server()
    clCLIENT.send_file()







if __name__ == "__main__":
    main()
