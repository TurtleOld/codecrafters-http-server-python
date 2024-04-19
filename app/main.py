# Uncomment this to pass the first stage
import socket
from _thread import start_new_thread


def client_handler(connection):
    while True:
        data = connection.recv(4096)
        
        if not data:
            break
        
        data = data.decode('utf-8')
        path = data.split()[1]
        if path == '/':
            response = 'HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n'
            connection.sendall(response.encode())
        elif path.startswith("/echo"):
            echo = path[6:]
            response = f'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(echo)}\r\n\r\n{echo}'
            connection.sendall(response.encode())
        elif path.startswith('/user-agent'):
            user_agent = data.split()[6] if len(data.split()) > 6 else ''
            response = f'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(user_agent)}\r\n\r\n{user_agent}'
            connection.sendall(response.encode())
        else:
            response = 'HTTP/1.1 404 Not Found\r\n\r\n'
            connection.sendall(response.encode())


def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    
    while True:
        connection, _ = server_socket.accept()
        start_new_thread(client_handler, (connection,))
        

if __name__ == "__main__":
    main()
