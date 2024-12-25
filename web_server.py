from socket import *

def createServer():
    server_socket = socket(AF_INET, SOCK_STREAM)
    try: 
        server_socket.bind(('localhost', 9000))
        server_socket.listen(5)
        while(1):
            (client_socket, address) = server_socket.accept()

            rd = client_socket.recv(5000).decode()
            pieces = rd.split("\n")
            if len(pieces) > 0: print(pieces[0])

            data = "HTTP/1.1 PK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            client_socket.sendall(data.encode())
            client_socket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error\n")
        print(exc)

    server_socket.close()

print("Access http://localhost:9000")

createServer()


            