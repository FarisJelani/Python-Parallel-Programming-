import socket
import threading
import random

# List of quotes
quotes = [
    "Love is about two side of respond the love, its same like serve>
    "In three words I can sum up everything I've learned about life:>
    "Strive not to be a success, but rather to be of value. - Albert>
    "Life is what happens when you're busy making other plans. - Joh>
    "The future belongs to those who believe in the beauty of their >
]

def handle_client(client_socket):
    # Get a random quote
    random_quote = random.choice(quotes)

    # Send the quote to the client
    client_socket.sendall(random_quote.encode())

    # Close the client socket
    client_socket.close()

def main():
    # Server information
    server_ip = "192.168.75.132"
    server_port = 8484

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address
    server_socket.bind((server_ip, server_port))


    # Listen for incoming connections
    server_socket.listen(5)
    print(f"QOTD Server listening on {server_ip}:{server_port}")

    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args>
        client_handler.start()

if __name__ == "__main__":
    main()

