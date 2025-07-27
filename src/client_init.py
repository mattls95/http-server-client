import socket
import os
import threading
from client import send_message, receive_message
from dotenv import load_dotenv

def init():
    try:
        load_dotenv(dotenv_path="../.env")
        HOST = os.environ.get("HOST")
        PORT = int(os.environ.get("PORT"))
        username = input("Enter username: ")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        threading.Thread(target=receive_message, args=(client, username)).start()
        threading.Thread(target=send_message, args=(client, username)).start()
    except KeyboardInterrupt:
        print("\nClient shutting down...")
        client.close()
        os._exit(0)

if __name__ == "__main__":
    init()