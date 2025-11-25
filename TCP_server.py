
import socket
#creating a server socket using AF_INET(IPV4) and SOCK_STREAM (TCP) 
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind or attaching the server socket to listen to incoming communication
#by defining its IP address and the port it should listen on for any incoming

#the host IP address can be hard coded or configured automatically 
#but automatically is better
#getting  the hostname
print (socket.gethostname())
#getting the ip address from the host name
print(socket.gethostbyname(socket.gethostname()))

#Binding our Socket to a tuple (IP ADDRESS,PORT NUMBER)
#the port number can be any as long as its not in use by the system
server_socket.bind((socket.gethostbyname(socket.gethostname()),12345))

#Putting the socket in the listening mode to listen for any connections

server_socket.listen()

#setting the server into listening and  mode continously for any connection
while True:
    #Accept any connection and storing two pieces of information
    client_socket,client_address=server_socket.accept()
    print(type(client_address),type(client_socket))
    print(client_address,client_socket)
    print(f'Connected to,{client_address}\n')

    #sending a message to the client that connected

    client_socket.send('YOU ARE CONNECTED'.encode('utf-8'))

    #close the connection once communication is done
    server_socket.close()
 #break out of the infinite loop else it will bring an error 
 #AN OPERATION WAS ATTEMPTED ON SOMETHING THAT IS NOT A SOCKET
    break