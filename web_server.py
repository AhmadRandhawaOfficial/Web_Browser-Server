from socket import *

def createServer():
    server_socket = socket(AF_INET, SOCK_STREAM)
    try: 
<<<<<<< HEAD
        server_socket.bind(('localhost', 9000))  # My computer, port number.
        server_socket.listen(5)  # if server busy, max 5 requests are placed in a backlog queue.
        while(1):
            (client_socket, address) = server_socket.accept()   # Wait for client to connect.
=======
        server_socket.bind(('localhost', 9000))
        server_socket.listen(5)
        while(1):
            (client_socket, address) = server_socket.accept()
>>>>>>> 7c0edc48b201389a6852f84375643247dc541215

            rd = client_socket.recv(5000).decode()
            pieces = rd.split("\n")
            if len(pieces) > 0: print(pieces[0])

<<<<<<< HEAD
            data = "HTTP/1.1 200 OK\r\n"
=======
            data = "HTTP/1.1 PK\r\n"
>>>>>>> 7c0edc48b201389a6852f84375643247dc541215
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


            