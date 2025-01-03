import socket


def server_program():
    host=socket.gethostname()
    port=5000

    #create socket instance
    server_socket=socket.socket()
    server_socket.bind((host,port))

    # listen to two connections
    server_socket.listen(2)
    conn,address=server_socket.accept()
    print('Connection from:{}'.format(str(address)))
    
    while True:
        # recieve data packet from client with max data packet size of 1024 bytes
        data=conn.recv(1024).decode()
        print(f'From Connected user: {data}')
        
        # if no data is recieved, break the loop
        if not data or data.lower().strip()=='bye':
            break
        response=input('=> ')
        #  sending response back to connected client in bytes
        conn.send(response.encode())
    conn.close()


if __name__=='__main__':
    server_program()


