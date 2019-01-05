import socket
from time import sleep

host = #Enter IP address of Raspberry pi,for example '192.168.10.100'
port = #Enter Port number, for example 9988(not in string format)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
command = #Enter the string or data you want to send
while True:
    s.send(str.encode(command))
    reply = s.recv(1024)
    print(reply)

s.close()
