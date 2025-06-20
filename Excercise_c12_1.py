import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd =  'GET /romeo.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n'.encode()
mysock.sendall(cmd)

mydata = str()
moredata = str()
while True:
    moredata = mysock.recv(512).decode()
    mydata += moredata
    if len(moredata) > 1:
        continue
    else: break
print(mydata)
mysock.close()
    


#had to do some practice for telnet
    #GET /Romeo.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n

'''GET /romeo.txt HTTP/1.1
Host: data.pr4e.org
Connection: close


GET /romeo.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n
GET http://data.pr4e.org/romeo.txt HTTP/1.0
'''