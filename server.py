from http.server import HTTPServer, BaseHTTPRequestHandler

messages = []

class chat_system(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        chat_history = "\n".join(messages) + "\n"
        self.wfile.write(chat_history.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8')
        
        if body.strip():
            messages.append(body.strip())
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Message sent successfully!\n")

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 5000), chat_system)
    print("Server running")
    server.serve_forever()
