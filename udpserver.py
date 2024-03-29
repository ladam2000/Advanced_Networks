##########################################################################
""" UDPServer.py                                     
Use the better name for this module:    MakeUpperCaseServerUsingUDP   
  
[STUDENTS FILL IN THE ITEMS BELOW]  
  STUDENT NAME                                 
  COURSE NAME and SEMESTER                    
  DATE                                         
  This module will <blah, blah, blah>              
"""

from socket import *
import time
def countdown(seconds):
    while seconds > 0:
        print(f"{seconds} másodperc a folytatásig...")
        time.sleep(1)
        seconds -= 1

# Futtassa a visszaszámlálást 10 másodpercre


# STUDENTS - you should randomize your port number.         
# This port number in practice is often a "Well Known Number" 
serverPort = 12000

# create UDP socket and bind to your specified port
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))

# output to console that server is listening
print ("The Make Upper Case Server running over UDP is ready to receive ... ")

while True:
    # read client's message AND REMEMBER client's address (IP and port)
    message, clientAddress = serverSocket.recvfrom(2048)

    # output to console the sentence received from client over UDP
    print("the ip address and port is ", clientAddress)
    # change client's sentence to upper case letters
    modifiedMessage = message.upper()
    # countdown(10)
    # send back modified sentence to the client using remembered address
    serverSocket.sendto(modifiedMessage, clientAddress)
 
    # output to console the modified sentence sent back to client
    print ("Sent back to Client: ", modifiedMessage)
    print()







