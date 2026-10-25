import socket
import threading
import sys

if len(sys.argv) < 3:
    print("Usage: python client.py <SERVER_IP> <YOUR_NAME>")
    sys.exit(1)

server_ip = sys.argv[1]
name = sys.argv[2]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, 5000))

def listen_for_messages():
    while True:
        try:
            print(client.recv(1024).decode('utf-8'))
        except:
            print("[Connection closed]")
            break

threading.Thread(target=listen_for_messages).start()

print(f"Connected as {name}")
while True:
    text = input()
    if text.strip():
        formatted_message = f"{name}: {text}"
        client.send(formatted_message.encode('utf-8'))
