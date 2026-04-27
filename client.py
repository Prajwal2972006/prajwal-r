import socket
import ssl

HOST = "10.1.6.20"   # Server laptop IP
PORT = 5000

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

secure_socket = context.wrap_socket(client_socket)

secure_socket.connect((HOST, PORT))

name = input("Enter player name: ")
score = input("Enter score: ")

message = name + "," + score

secure_socket.send(message.encode())

data = secure_socket.recv(4096)

print(data.decode())

secure_socket.close()