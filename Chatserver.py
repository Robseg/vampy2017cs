import socket
import time
ids = [4, 8, 16]
addr = (socket.gethostname(), 8080)
phone = socket.socket()
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
phone.bind(addr)
phone.listen(128)
while True:
	try:
		conn, cid = phone.accept()
		msg = bytes.decode(conn.recv(1024))
		conn.send("r".encode("UTF-8"))
		conn.close()
		print("Call from {0}: {1}.".format(cid, msg))
		data = msg.encode("UTF-8")
		relay = socket.socket()
		for i in ids:
			respond = ("vampy-cs-"+str(i), 8080)
			relay.connect(respond)
			relay.send(data)
			relay.close()
			time.sleep(0.1)
	except KeyboardInterrupt:
		print("Shutting down gracefully...")
		phone.close()
		break
	except Exception as e:
		print(e)
		print("Something unexpected happened, shutting down...")
		phone.close
		break


