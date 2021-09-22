import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()        
print ("chat server is active")
port = 12345 
s.bind(('', port))        
s.listen(5)     
c, addr = s.accept()    
print ('Client is online', addr )  


def send_msg():
	msg = input("send msg: >> ")
	b = bytes(msg, 'utf-8')
	c.send(b)


def recv_msg():
	msg2 = c.recv(1024)
	print("recv msg: >>" + msg2.decode('UTF-8'))
	

while True:
	send_msg()
	recv_msg()
