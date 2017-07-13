import socket

address = input("Enter an Address")
port = int(input("Enter a port"))

s = socket.socket()

s.connect((address,port))

while True:
	message = input("Enter a message.")
	s.sendall(message.encode("utf-8"))

