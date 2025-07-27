def receive_message(client,username):
    while True:
        try:
            message = client.recv(1024)
            if message == 'USER':
                client.send(username.encode())
            else:
                print(message.decode())
        except Exception:
            print("Disconncted from server")
            client.close()
            break

def send_message(client, username):
    while True:
        user_input = input("")
        if user_input.strip() == "":
            continue  # Skip sending empty messages
        message = f"{username}: {user_input}"
        client.send(message.encode())