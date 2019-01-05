import socket
import time

host = #Enter IP address of Raspberry pi,for example '192.168.10.100'
port = #Enter Port number, for example 9988(not in string format)

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind complete.")
    return s

def setupConnection():
    s.listen(1) # Allows one connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

def dataTransfer(conn):
    while True:
        data = conn.recv(1024) # receive the data
        data = data.decode('utf-8')
        print(data)
    conn.close()

s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break
