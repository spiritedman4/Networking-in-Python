import threading
import socket


nickname=input('Enter a nickname: ')

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',55555))


def recieve():
    while True:
        try:
            message=client.recv(1024).decode()
            if message =='NICK':
                client.send(nickname.encode())
            else:
                print(message)
        except:
            print('Error Occured')
            client.close()
            break


def send():
    while True:
        message=f'{nickname}: {input()}'
        client.send(message.encode())


def start_client():
    recieve_thread=threading.Thread(target=recieve,args=())
    recieve_thread.start()

    send_thread=threading.Thread(target=send,args=())
    send_thread.start()

start_client()