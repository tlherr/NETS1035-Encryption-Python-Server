import socket
import time 

secure_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

secure_socket.bind(('0.0.0.0', 8886))

secure_socket.listen(1)
print("Waiting for a client ")
(clientsocket, address) = secure_socket.accept()
received = clientsocket.recv(400)
print(received.decode()) 
clientsocket.sendall(b'welcome')
print("Received ")
time.sleep(2)

while True:
	data = clientsocket.recv(400)
	print(data.decode())
	clientsocket.sendall(b'got it')	
	time.sleep(2)
