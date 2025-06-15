import socket
import threading

# Server Information
HOST = '127.0.0.1'  # Localhost (use your local machine's IP for remote clients)
PORT = 5050         # Choose an available port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

# Function to broadcast messages to all connected clients
def broadcast(message, _client):
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except:
                pass

# Handle each client connection
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            if client in clients:
                index = clients.index(client)
                nickname = nicknames[index]
                clients.remove(client)
                nicknames.remove(nickname)
                broadcast(f"{nickname} has left the chat.".encode('utf-8'), client)
                print(f"{nickname} disconnected.")
                client.close()
            break

# Accept clients and start threads
def receive():
    print(f"Server running on {HOST}:{PORT}")
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname: {nickname}")
        broadcast(f"{nickname} has joined the chat.".encode('utf-8'), client)
        client.send("Connected to server!".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
