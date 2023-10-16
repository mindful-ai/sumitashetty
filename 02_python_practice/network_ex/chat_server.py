import socket


def server_program():
    # get the hostname
    host = '127.0.0.1'
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(5)

    # -------------------------------------------------------------------
    # accept new connection
    conn, addr = server_socket.accept()
    # print connection details
    print('Connection Received from: ', str(addr))

    while True:
        
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        # if data is not received break
        if not data:
            break
        # Print received data
        print('Received from Client -> ', data)
        # input the data from the user
        
        data = input("-> ")
        # send data to the client
        conn.send(data.encode())
        
    # ------------------------------------------------------------------------

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()