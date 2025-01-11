import socket

host='127.0.0.1'
port=9997

# SOCK_DGRAM is UDP Socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

try:
    client.sendto('Hello World!'.encode(),(host,port))
    data,addr=client.recvfrom(4096)
    print(f'{data.decode()} from {str(addr)}')
except:
    client.close()
