import socket
import time 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('192.168.161.132', 8886)
sock.connect(server_address)
sock.sendall(b'hello')
message = sock.recv(1000)
sock.sendall(b'ok')
print(message.decode())
print(len(message))
sock.sendall(b'Hi')
response = sock.recv(16)
while True:    
	print("Received" + str(response))
	myinput=input("send some data ")
	sock.sendall(myinput.encode())
	response = sock.recv(32)
