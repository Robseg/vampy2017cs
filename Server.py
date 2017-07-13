import socket
while True:
	N = (input("Who do you want to call?"))
	msg = input("What is your message?")
	data = msg.encode("UTF-8")
	addr = ("vampy-cs-"+N, 4242)
	phone = socket.socket()
	try:
		phone.connect(addr)
		phone.send(data)
		resp = bytes.decode(phone.recv(1024))
		if resp != "r":
			print("Woops!")
		phone.close()
