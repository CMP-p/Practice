#I practice in here with the lesson
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(mysock)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET /romeo.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()
mysock.send(cmd)

dati = b''
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    dati += data
mysock.close()


print(dati.decode())

# Pracrticing with TCP? something about sockets, ports and extensions
# recieving byte strings, looping through data and decoding the results