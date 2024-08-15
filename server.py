from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        url = urllib.parse.parse_qs(post_data.decode('utf-8'))['url'][0]
        
        # Save the URL to a variable or process it as needed
        changed(url)


        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'URL received')
    def log_message(self, format, *args):
        return

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

from main import changed