import http.server
import socketserver
import datetime

PORT = 8082

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("Server running on port", PORT)
today = datetime.date.today()
print (today.strftime("%m/%d/%Y"))  

httpd.serve_forever()
# Starts server
# http://127.0.0.1:8082
# Uses index.html file in the directory that this file is in.
