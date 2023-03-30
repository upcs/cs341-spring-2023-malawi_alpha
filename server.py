#!/usr/bin/env python3
#handles the cgi scripts, and the server
import http.server
import os
import socketserver

#change the directory to the project directory
#this probably needs to be tweaked
os.chdir("path/to/your/project")

Handler = http.server.CGIHTTPRequestHandler
Handler.cgi_directories = ['/cgi-bin']

PORT = 8000

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving on port", PORT)
    httpd.serve_forever()
