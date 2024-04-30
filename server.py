import http.server
import socketserver
import os

PORT = 8000 # Website will be available at http://localhost:8000/

# Get the current directory (where your build.py  is located)
current_directory = os.getcwd()

# Set the current directory as the working directory for the HTTP server
os.chdir(current_directory+'/public')

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
