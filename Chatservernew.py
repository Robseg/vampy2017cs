import socket

address = ""
port = int(input("Enter a port to host on: "))

s = socket.socket()

s.bind((address,port))#Bind till connection

s.listen(8)

conn, addr = s.accept() #Pause until connect

def handle_connection():
	while True:
		data = conn.recv(1024)
		print(data.decode("utf-8"))
while True:
	conn, addr = s.accept() #Pause until connect
	_thread.start_new_thread(handle_conncection

