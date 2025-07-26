import socket
import os
from server import receive_new_clients

def init():
    HOST = os.environ.get("HOST")
    PORT = os.environ.get("PORT")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    receive_new_clients(server, HOST, PORT)