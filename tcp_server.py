import socket
import os

def tcp_server(host='127.0.0.1', port=65432):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("TCP Server is listening...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Receive file size
    file_size = int.from_bytes(conn.recv(4), 'big')
    # Receive file name
    file_name = conn.recv(64).decode().strip('\x00')

    # Receive file data
    with open(file_name, 'wb') as f:
        bytes_received = 0
        while bytes_received < file_size:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
            bytes_received += len(data)

    print(f"Received file: {file_name} ({file_size} bytes)")
    conn.close()
    server_socket.close()

# Start the TCP server
if __name__ == "__main__":
    tcp_server()