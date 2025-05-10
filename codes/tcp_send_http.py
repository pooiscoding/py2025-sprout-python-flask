import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = "www.ntu.edu.tw"
server_port = "80"

try:
    sock.connect((server_ip, int(server_port)))
except Exception as e:
    print(f"Connection failed\nError: {e}")
    exit(1)

req = "GET / HTTP/1.1\r\n\r\n"

sock.sendall(req.encode())
response = sock.recv(1024).decode()
print(response)

sock.close()