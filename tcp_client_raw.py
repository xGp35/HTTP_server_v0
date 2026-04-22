import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9000))

client.send(b"RAW TCP TEST")

client.close()