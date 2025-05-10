import socket
import select

HOST = '0.0.0.0'
PORT = 5522
BUFFER_SIZE = 1024
QUEUED_CONNECTIONS = 30

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(QUEUED_CONNECTIONS)

inputs = [server_socket]
outputs = []

print(f"Server is listening on {PORT}...")

with open("logfile.txt", "w") as f:
    f.write("")

file = open("logfile.txt", "a", encoding="utf-8")

while True:
    readable, _, exceptional = select.select(inputs, outputs, inputs)

    for s in readable:
        if s is server_socket:
            client_socket, client_address = s.accept()
            print(f"New connection from {client_address}")
            inputs.append(client_socket)
        else:
            data = s.recv(BUFFER_SIZE)
            msg = data.decode("utf-8").strip()
            if data:
                file.write(msg + "\n")
                file.flush()
                s.sendall(f"Received Your Message: {msg}\n".encode("utf-8"))
            else:
                inputs.remove(s)
                s.close()

    for s in exceptional:
        inputs.remove(s)
        s.close()

file.close()