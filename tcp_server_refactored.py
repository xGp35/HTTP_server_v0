import socket
import time

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 9000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Add some optionsal settings to change the default behaviour of sockets
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.setblocking(True)
# Blocking mode, so the statements in except block don't run

server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)
# The backlog parameter = 5, tells use the maximum number of fully established connections that can wait in the queue.


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
        request = data.decode()
        print(request)
        headers = request.split('\n')
        first_header_components = headers[0].split()
        http_method = first_header_components[0]
        path = first_header_components[1]

        if http_method == 'GET':
            if path == '/':
                fin = open('index.html')
            elif path == '/book':
                fin = open('book.json')
            else:
                response = 'HTTP/1.1 404 Not Found\n\n'
            content = fin.read()
            fin.close()
            response = 'HTTP/1.1 200 OK\n\n' + content
        else:
            response = 'HTTP/1.1 405 Method Not Allowed\n\nAllow: GET'
        client_socket.sendall(response.encode())
        client_socket.close()
    except BlockingIOError:
        time.sleep(2)
        continue
