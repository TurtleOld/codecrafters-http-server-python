# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    connection, address = server_socket.accept()
    with connection:
        print("Connected by", address)
        while True:
            data = connection.recv(1024)
            if not data:
                break
            path = data.decode().split()[1]
            if path == "/":
                connection.send(b'HTTP/1.1 200 OK\r\n\r\n')
            elif path.startswith("/echo"):
                echo = path[6:]
                response = f'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(echo)}\r\n\n{echo}\r\n\r\n'
                connection.send(response.encode())
            else:
                connection.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
            

if __name__ == "__main__":
    main()
