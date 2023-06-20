# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:19:52 2023

@author: Shane
"""

import socket as socket



""" Using python command list all the methods inside the Socket module."""
#print(dir(socket))

""" Write a Python script to ask user for a list of port numbers and check those services in the local host."""

"""ip ='127.0.0.1' #Localhost IP Address

portlist = [] #Empty array to store values
for i in range(3): # Loop 3 times
    userInput = input("Which ports do you want to check?") #Prompt user for port numbers

    portlist.append(int(userInput)) #Append user input to array


print(portlist) #Print ports to confirm succesfull input
for port in portlist:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Setting up TCP saocket to establish a connection
    result = sock.connect_ex((ip,port)) #Store result and take in IP and Port
    print(port,":", result) #Print port number and the status to user
    print("Checking ports...")
    if result == 10061: #If port is closed...
        print("Connection Refused.") #Inform user
    else: #Otherwise
        print("Connection accepted.") #Inform user port is open
    sock.close()  #Close socket once selected ports have been scanned
"""

"""3- Write a Python script to implement a server listening on port 443. The sever accepts maximum 10
requests. Server should reply to client with “You are connected to the server!”.

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Open socket for connection
mySocket.bind(('localhost', 443)) #Bind socket  to localhost and port 443

mySocket.listen(5) #Server will listen for five seconds

while True:
    print("Waiting for connections...")
    (recvSocket, address) = mySocket.accept() #Accepting connections using .accept(), parsing  recvSocket and address
    print("HTTP request received:") 
    print(recvSocket.recv(1024)) #
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n <html><body><h1>Connection recevied!</h1></body></html> \r\n", 'utf-8')) #Respond with a HTML pagee
    recvSocket.close() #Close socket connection
    


#4- Using Python write a client to connect to the server create in exercise 3 and retrieve the data from
#server

webhost = "localhost"
webport = 443

print("Contacting %s on port %d ... "% (webhost,webport)) 
webclient = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
webclient.connect((webhost,webport)) #Create webclient connection using localhost and port 443
webclient.send(bytes("GET / HTTP/1.1\r\nHost: localhost\r\n\r\n".encode('utf-8'))) #HTTP Get request to server
reply = webclient.recv(4096)  #Receive a 4096 byte reply on the webclient
print("Response from %s:"% webhost) #Print response from server
print(reply.decode()) #Decode response

"""

#5- Using Python retrieve the IP address of the following websites"""

try:
    print("getaddrinfo for GCU",socket.getaddrinfo("www.gcu.ac.uk",None,0,socket.SOCK_STREAM))
    print("getaddrinfo for CNN",socket.getaddrinfo("www.cnn.com",None,0,socket.SOCK_STREAM))
    print("getaddrinfo for BBC",socket.getaddrinfo("www.bbc.com",None,0,socket.SOCK_STREAM))
    

    
except socket.error as error:
    print(str(error))
    print("Connection error")

#6- Write a Python code to accept an IP address and look up the hostname.

userIP = input("Enter the IP you wish to scan:")

print("gethostbyaddr:",socket.gethostbyaddr(userIP))


