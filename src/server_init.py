import socket
import os
from server import receive_new_clients
from dotenv import load_dotenv

def init():
    try:
        load_dotenv(dotenv_path="../.env")
        HOST = os.environ.get("HOST")
        PORT = int(os.environ.get("PORT"))
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        receive_new_clients(server, HOST, PORT)
    except Exception:
        print("\nServer shutting down...")
        server.close()
        os._exit(0)

if __name__ == "__main__":
    init()