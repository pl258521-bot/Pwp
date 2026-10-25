import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5000))
server.listen()

clients = []

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            for c in clients:
                if c != client:
                    c.send(message)
        except:
            clients.remove(client)
            client.close()
            break

print("Server active")
while True:
    client_socket, _ = server.accept()
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket,)).start()
