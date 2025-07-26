import threading

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

def receive_new_clients(server, HOST, PORT):
    server.listen()
    print(f"Server running on{HOST}:{PORT}")

    while True:
        client,address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("User")
        username = client.recv(1024)
        usernames.append(username)
        clients.append(client)

        print(f"user is {username}")
        send_message(f"{username} joined the chat")
        client.send("Connected to the server")

        thread = threading.Thread(target=handle, args=(client,))
        thread.start
