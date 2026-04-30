import socket

HOST = "0.0.0.0"
PORT = 9000

response_body = b"x" * 1024 * 1024 * 5  # 5 MB fake file

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("Server running on port 9000...")

while True:
    client_socket, addr = server_socket.accept()
    request = client_socket.recv(1024).decode()

    print("\n--- Request ---")
    print(request)

    method = request.split(" ")[0]

    headers = (
        "HTTP/1.1 200 OK\r\n"
        f"Content-Length: {len(response_body)}\r\n"
        "Content-Type: application/octet-stream\r\n"
        "\r\n"
    )

    client_socket.sendall(headers.encode())

    if method == "GET":
        client_socket.sendall(response_body)

    client_socket.close()