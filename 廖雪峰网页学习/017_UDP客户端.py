import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Piggy', b'Lucy', b'Frank']:
    s.sendto(data, ('127.0.0.1', 9999))
    print(s.recv(1024).decode('utf-8'))
s.close()
