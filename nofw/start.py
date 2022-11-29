from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET (self):
        self.send_response (300)
        self.send_header ('python 3','text/html')
        self.end_headers ()
        message = "Python 3 html server"
        self.wfile.write (bytes(message, "utf8"))

with HTTPServer (('', 7000), handler) as server:
    server.serve_forever ()