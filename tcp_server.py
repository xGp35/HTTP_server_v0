import socket
import time

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 9000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Add some optionsal settings to change the default behaviour of sockets
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.setblocking(True)


server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)
# The backlog parameter = 5, tells use the maximum number of fully established connections that can wait in the queue.


response_body = "Hello Client Hello Client Hello Client"

response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/plain\r\n"
    f"Content-Length: {len(response_body)}\r\n"
    "\r\n"
    f"{response_body}"
)
# while True:
#     try:
#         client_socket, client_address = server_socket.accept()
#         print(f"Client Socket: {client_socket}")
#         print(f"Connected by: {client_address}")
#     except:
#         time.sleep(1)
#         print("I am in except block")
#         continue    


while True:
    print("Waiting for client...")
    try:
        client_socket, client_address = server_socket.accept()
        # accept() says: “Pause here until someone connects.”
        # accepts any TCP connection, not specifically HTTP.
        # but if conection is set to non blocking, then this line will throw an error if there are no connection in queue.
        # browsers communicate using the HTTP protocol over TCP, Brave connected and sent an HTTP request.

        print(f"Client Socket: {client_socket}")
        print(f"Connected by: {client_address}")
        # Till this much I am just starting a TCP server.

        data = client_socket.recv(1024)
        # recv() means: “Wait and read incoming data from the client.”
        # Receive up to 1024 bytes of data from the connected client.
        print("Decoding data...")
        print(data.decode())

        client_socket.send(response.encode())

        client_socket.close()
    except:
        time.sleep(2)
        continue


# Some clients are lenient, but official HTTP specification expects:
# CRLF = \r\n
# So when building HTTP manually, always use \r\n.

# What .encode() does? It converts a string into bytes, usually using UTF-8 by default.

#Sockets work at the network level, where data is just sequences of bytes—not Python text objects.
#HTTP messages, TCP packets, etc., are all ultimately transmitted as bytes.
# So, str  → encode() → bytes → send()
