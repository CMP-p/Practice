import socket
#importing the socket library
Mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#calling the socket library, then the socket function/class constructor. Then calling 2 special variables in the library
Mysock.connect(('data.pr4e.org', 80))
#connecting the socket to the website on port 80 which is typical for html ports does 

'''
Does the RandomSocket.Conntect function, create the "line of communication" between the socket/port on my computer to
the server that I've identified? Could I replace 'data.py4e.org' with the server addres? 
Yes, appearently i can'''

cmd = 'GET /romeo.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()
Mysock.sendall(cmd)


'''
Okay, but how about .recieve()? if i send nothing, what will be recieved? what if I've recieved all, will noting more be
recieved? What if i send something but never recieve. What if i send something invalid, and then something valid, and then 
recieve, will I recieve both portions of data?'''
'''
You'll get a server error. This specific example, the serrver will close your connection and not listesn for new requests
and depending on the error, will give you an error 400, bad request, or error 501, not implemented
'''


data2print = str()
while True:
    data = Mysock.recv(512).decode()
    if len(data) < 1:
        break
    else: data2print += data
    print(data2print)

'''while True:
    data = Mysock.recv(512).decode()
    if len(data) > 1:
        print(data)
    else: break
    (alternate code block)
    '''
Mysock.close()


#I was doing some testing around, building comprehension on sockets. Even though they aren't used. I wanted to refound myself 
#before moving further ahead. 