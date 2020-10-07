import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) # Start the calling to the web page in the port 80
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() 
# Say hello and wait for a response
mysock.send(cmd)
# Get the response
while True:
    data = mysock.recv(512) # read 512 bytes at a time
    if (len(data) < 1): #  When nothing more to read
        break
    print(data.decode())

mysock.close()
