import socket

# Server address and port (replace with actual EC2 instance IP)
HOST = "13.234.38.90"
PORT = 5000

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Receive uptime data
data = client_socket.recv(1024).decode()
print(data)

# Close the connection
client_socket.close()

print("Client disconnected")



