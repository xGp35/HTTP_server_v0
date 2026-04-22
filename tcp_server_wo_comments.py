import socket

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 9000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)


print("Waiting for client...")
client_socket, client_address = server_socket.accept()


print(f"Client Socket: {client_socket}")
print(f"Connected by: {client_address}")

data = client_socket.recv(1024)


print("Decoding data...")
print(data.decode())

response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/plain\r\n"
    "Content-Length: 12\r\n"
    "\r\n"
    "Hello Client"
)
client_socket.send(response.encode())

client_socket.close()
server_socket.close()









