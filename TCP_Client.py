#importing the socket module
import socket
#Creating client socket using AF_INET and SOCK_STREAM
Client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Connecting the socket to a server located at a given IP and PORT
Client_socket.connect((socket.gethostbyname(socket.gethostname()),12345))

#Receive a message from TCP_Server specifying 
# the maximum number of bytes to recevr

message=Client_socket.recv(1024)
print(type(message),message)
Client_socket.close()