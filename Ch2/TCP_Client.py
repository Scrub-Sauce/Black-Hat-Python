import socket

target_host = "0.0.0.0"
target_port = 9998

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the client
client.connect((target_host, target_port))

# Send some data
client.send(b"ABCDEFG")

# Recieve some data
response = client.recv(4096)

print(response.decode())
client.close()