import socket

testcases = [ 
    "add,12,13",
    "sub,12,13",
    "mul,12,13",
    "div,12,13"
]
def client_program():
    host = '192.168.0.114'  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    # ---------------------------------------------------------------

    for testcase in testcases:
        # send test data
        client_socket.send(testcase.encode())

        # receive response
        data = client_socket.recv(1024).decode()
            
        # show in terminal
        print('Received from Server -> ', data)

    # ---------------------------------------------------------------

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()

