import socket


def client_program():
    host = '127.0.0.1'  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    # ---------------------------------------------------------------

    # take user input
    mess = input("-> ")

    while mess.lower().strip() != 'quit':
        # send message
        client_socket.send(mess.encode())

        # receive response
        data = client_socket.recv(1024).decode()
        # show in terminal
        print('Received from Server -> ', data)

        # Repeat
        mess = input("-> ")

    # ---------------------------------------------------------------


    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()

