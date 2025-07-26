import socket
import threading

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 1024  # Port to listen on (non-privileged ports are > 1023)

clients = []
usernames =[]

def send_message(message):
    for client in clients:
        try:
            client.send(message)
        except Exception:
            client.close()

def recieve_message(client):
    while True:
        try:
            message = client.recv(1024)
            send_message(message)
        except Exception:
            remove_client(client)
            break

def remove_client(client):
    index = clients.index(client)
    clients.remove(client)
    client.close()
    username = username[index]
    print(f"{username} disconnected")
    send_message(f"{username} has left the chat")
    usernames.remove(username)

def receive_new_clients(server):
    server.listen()
    print(f"Server running on{HOST}:{PORT}")

    while True:
        client,address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("User")
        username = client.recv(1024)
        usernames.append(username)
        clients.append(client)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)