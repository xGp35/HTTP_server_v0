from http.server import HTTPServer, BaseHTTPRequestHandler
import time
import json

HOST = "192.168.1.3"
PORT = 9999

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        with open('index.html', 'r', encoding = 'utf-8') as f:
            html_content = f.read()

        self.wfile.write(html_content.encode('utf-8'))
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        response = {
            "time": date
        }

        self.wfile.write((json.dumps(response) + "\n").encode('utf-8'))

server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Server now Running...")
server.serve_forever()
server.server_close()

print("Server stopped ...")