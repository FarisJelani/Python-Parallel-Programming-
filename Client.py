import socket

def main():
    # Server information
    server_ip = "192.168.75.132"
    server_port = 8484

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_ip, server_port))
    print(f"Connected to the QOTD server at {server_ip}:{server_port}")

    # Receive and display the quote from the server
    quote_data = client_socket.recv(1024).decode()
    print(f"Quote of the Day: {quote_data}")

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    main()
