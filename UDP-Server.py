import socket

host='127.0.0.1'
port=9997

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((host,port))
print(f'Binded to the {port} on {host}')
while True:
    data,addr=server.recvfrom(1024)
    print(f'{data.decode()} from {str(addr)}')
    if data:
        server.sendto(data,addr)
        print(f'Sending data back to the {str(addr)}')

    
