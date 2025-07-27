import threading

clients = []
usernames =[]

def send_message(message):
    for client in clients:
        try:
            client.send(message.encode())
        except Exception as e:
            print(f"Error: {e}")
            client.close()

def recieve_message(client):
    while True:
        try:
            message = client.recv(1024).decode()
            send_message(message.encode())
        except Exception as e:
            print(f"Error: {e}")
            remove_client(client)
            break

def remove_client(client):
    index = clients.index(client)
    clients.remove(client)
    client.close()
    username = usernames[index]
    print(f"{username} disconnected")
    send_message(f"{username} has left the chat")
    usernames.remove(username)

def receive_new_clients(server, HOST, PORT):
    server.listen()
    print(f"Server running on HOST: {HOST} PORT: {PORT}")

    while True:
        client,address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("USER".encode())
        username = client.recv(1024).decode()
        usernames.append(username)
        clients.append(client)

        client.send("Connected to the server\n".encode())
        send_message(f"{username} joined the chat\n")
        

        thread = threading.Thread(target=recieve_message, args=(client,))
        thread.start()
