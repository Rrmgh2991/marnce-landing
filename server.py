import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 8080))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "":
            self.path = "/index.html"
        return super().do_GET()

    def log_message(self, format, *args):
        pass

httpd = socketserver.TCPServer(("0.0.0.0", PORT), Handler)
print(f"Server running on port {PORT}")
httpd.serve_forever()
