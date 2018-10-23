#!/usr/bin/env python
 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8080)

handler.http_directories = ["/","/catasto_2016","/data","/cust_tiles"]
handler.cgi_directories = ["/normalizza_vie","/cgi-bin"]
 
httpd = server(server_address, handler)
try:
   httpd.serve_forever()
except KeyboardInterrupt:
   httpd.socket.close()

