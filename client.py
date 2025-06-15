import socket

# now we get our client side app work

HOST ="0.0.0.0"
PORT = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))


sock.send("server says hi".encode())

sock.close()

