import socket

#now we get the host and port to cbind

HOST = "0.0.0.0"
PORT = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now we connect

server.bind((HOST, PORT))
server.listen(5) # 5 s=connections at a time

print(f"Server listening on {HOST} at port {PORT}")
print("waiting for client to connect")


# now we gotta accept a ny client 
client_socket, client_adress = server.accept()
print(f"connection from {client_socket} {client_adress} [data]")


#now lets send something

client_socket.send("server says hello client".encode())

data = client_socket.recv(1024).decode()

print(data)


client_socket.close()
server.close()
