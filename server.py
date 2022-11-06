import socket

HOST = "192.168.1.2" #change to your ipv4 wifi address
PORT = 5050
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(1)
conn, addr = server.accept()
#handle_game --function to handle game

#copied from sample
with conn:
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        print(data)
        if not data:
            break
        conn.sendall(data)
    