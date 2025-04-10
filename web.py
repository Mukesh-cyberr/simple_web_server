from http.server import HTTPServer,BaseHTTPRequestHandler
content='''
<!doctype html>
<html>
    <head>
        <title>
            TCP/IP
        </title>
    </head>
    <body bgcolor="pink">
        <center><h1>TCP/IP PROTOCALS<br></h1></center>
        <br>
        1. Application Layer HTTP,FTP,SSH, Telnet & DNS <br> 2. Transport layer TCP,UDP <br>
        3. Internet layer ICMP,IGMP,ARP,IPv4/IPv6<br>4. Network access layer Ethernet,FDDI,X 25, FRAAME RELAY,TOKEN RING

    </body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()