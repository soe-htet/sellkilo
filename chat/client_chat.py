
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.0.1.48', 8888)) #IP is the server IP

for args in sys.argv:
    if args == "":
        args = 'no args'
    else:
        s.send(args + ' ')

print("good bye")
