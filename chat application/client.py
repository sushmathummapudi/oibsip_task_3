import socket
import threading

HOST = '127.0.0.1'  # Use the same HOST as server
PORT = 5050         # Use the same PORT as server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Choose nickname
nickname = input("Choose your nickname: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Disconnected from server.")
            client.close()
            break

def write():
    while True:
        try:
            message = input()
            client.send(f"{nickname}: {message}".encode('utf-8'))
        except:
            break

# Start threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
