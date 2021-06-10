import socket 
hostname = socket.gethostname()
Ipadr= socket.gethostbyname( hostname)
print("ip address is :"+ Ipadr)
