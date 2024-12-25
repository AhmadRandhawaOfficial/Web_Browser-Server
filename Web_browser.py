import socket   # The socket is like a phone, it allows your comp to talk to other comp over the internet

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Used IPv4 & TCP/IP for communication.
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())    # Ensures print adds no \n at the end of the line 

mysock.close()