import threading
import socket


host='127.0.0.1' #localhost
port=55555

# create a socket instance
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # AF_INET is the address family for IPv4 uses internet socket. SOCK_STREAM is the socket type for TCP
server.bind((host,port))
server.listen()
print('Connection Ready to Accept')


clients=[]
nicknames=[]


# broadcast messages among clients
def broadcast(message,msg_client):
    for client in clients:
        if msg_client != client:
            client.send(message.encode())



def handle(client):
    while True:
        try:
            message=client.recv(1024).decode()
            broadcast(message,client)
        except:
            index=clients.index(client)
            nickname=nicknames[index]
            clients.remove(client)
            nicknames.remove(nickname)
            message=f'{nickname} is out'
            broadcast(message,client)
            client.close()
            break

# listening handler for server
def recieve():
        while True:
            client,address=server.accept()
            client.send('NICK'.encode())
            
            # asks for nickname
            nick=client.recv(1024).decode()
            clients.append(client)
            nicknames.append(nick)

            # broadcast message
            print(f'{nick} is connected to the server')
            broadcast(f'{nick} joined us guys.',client)
            client.send('Connected to the server successfully.'.encode())

            # creates a thread for every client
            thread=threading.Thread(target=handle,args=(client,))
            thread.start()

recieve()