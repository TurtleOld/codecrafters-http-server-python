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
            header = parse_header(data.decode("utf-8"))
            if header.path == b'/':
                connection.send(b'HTTP/1.1 200 OK\r\n\r\n')
            else:
                connection.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
            

if __name__ == "__main__":
    main()
