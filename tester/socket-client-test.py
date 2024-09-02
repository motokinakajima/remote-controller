import socket

def run_client():
    # Set up the socket server
    #==================================
    server_address = 'kpc.local'
    server_port = 11452
    #==================================

    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Connect to the server
        client_socket.connect((server_address, server_port))
        print(f"Connected to server at {server_address}:{server_port}")

        # Prompt the user for input
        message = input("Enter the message to send to the server: ")
        
        # Send data to the server
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent: {message}")

if __name__ == "__main__":
    while True:
        run_client()
