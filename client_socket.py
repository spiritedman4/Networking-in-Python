import socket

def client_program():
    hostname=socket.gethostname()
    port=5000

    # create socket instance
    client_socket=socket.socket()

    # connect to the server
    client_socket.connect((hostname,port))
    message=input('=> ')

    # this loop will run until the client types 'bye'
    while message.lower().strip()!='bye':
        # this sends data to the host
        client_socket.send(message.encode())

        # this recieves data packets within 1024 bytes or won't accept packets greater than it.
        response=client_socket.recv(1024).decode()
        print(f'Server Response: {response}')
        message=input('=> ')
        client_socket.send(message.encode())
    
    client_socket.close()





if __name__=='__main__':
    client_program()