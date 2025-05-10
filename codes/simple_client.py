import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = input("Enter server IP: ")
server_port = input("Enter server port: ")

try:
    sock.connect((server_ip, int(server_port)))
except Exception as e:
    print(f"Connection failed\nError: {e}")
    exit(1)

name = input("Enter your name: ")

sock.sendall(name.encode("utf-8"))
response = sock.recv(1024).decode("utf-8").strip()
print(f"Server says [ {response} ]")

sock.close()