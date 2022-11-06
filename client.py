import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("192.168.1.2", 5050)) #change to your ipv4 wifi address

#copied from sample
conn.sendall(b"has connected")
data = conn.recv(1024)

print(f"Received {data!r}")