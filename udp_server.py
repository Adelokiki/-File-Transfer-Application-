import socket

def udp_server(host='127.0.0.1', port=65432):
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print("UDP Server is listening...")

    while True:
        # Receive file size
        file_size, addr = server_socket.recvfrom(4)
        file_size = int.from_bytes(file_size, 'big')

        # Receive file name
        file_name, addr = server_socket.recvfrom(64)
        file_name = file_name.decode().strip('\x00')

        # Receive file data
        with open(file_name, 'wb') as f:
            bytes_received = 0
            while bytes_received < file_size:
                data, addr = server_socket.recvfrom(1024)
                if not data:
                    break
                f.write(data)
                bytes_received += len(data)

        print(f"Received file: {file_name} ({file_size} bytes) from {addr}")

# Start the UDP server
if __name__ == "__main__":
    udp_server()