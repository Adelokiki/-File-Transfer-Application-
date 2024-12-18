import socket
import os

def tcp_client(file_path, host='127.0.0.1', port=65432):
    try:
        # Create a TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        # Get file size and name
        file_size = os.path.getsize(file_path)
        file_name = os.path.basename(file_path)

        # Send file size
        client_socket.send(file_size.to_bytes(4, 'big'))
        # Send file name
        client_socket.send(file_name.encode().ljust(64, b'\x00'))

        # Send file data
        with open(file_path, 'rb') as f:
            data = f.read(1024)
            while data:
                client_socket.send(data)
                data = f.read(1024)

        print(f"Sent file: {file_name} ({file_size} bytes)")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()

# Call the tcp_client function with the path to your file
tcp_client(r"C:\Users\HP\Desktop\my project vscode\test_file.txt")