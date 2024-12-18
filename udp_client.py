import socket
import os

def udp_client(file_path, host='127.0.0.1', port=65432):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Get file size and name
    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)

    # Send file size
    client_socket.sendto(file_size.to_bytes(4, 'big'), (host, port))
    # Send file name
    client_socket.sendto(file_name.encode().ljust(64, b'\x00'), (host, port))

    # Send file data
    with open(file_path, 'rb') as f:
        data = f.read(1024)
        while data:
            client_socket.sendto(data, (host, port))
            data = f.read(1024)

    print(f"Sent file: {file_name} ({file_size} bytes)")
    client_socket.close()

# Call the udp_client function with the path to your file
udp_client(r"C:\Users\HP\Desktop\my project vscode\test_file.txt")