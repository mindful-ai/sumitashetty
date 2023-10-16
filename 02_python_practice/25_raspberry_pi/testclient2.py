import sys
import random

import socket

import unittest

FAILURE = ''

host = '192.168.1.105'  # as both code is running on same pc
port = 5000  # socket server port number
client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

class CalculatorTest(unittest.TestCase):



    def test_add(self):
        v1 = random.randint(1, 100)
        v2 = random.randint(1, 100)
        eval = float(v1 + v2)
        testcase = ','.join(['add', str(v1), str(v2)])
        client_socket.send(testcase.encode())
        oval = float(client_socket.recv(1024).decode())
        print(oval, eval)
        self.assertEqual(eval, oval, FAILURE)

    def test_sub(self):
        v1 = random.randint(1, 100)
        v2 = random.randint(1, 100)
        eval = float(v1 - v2)
        testcase = ','.join(['sub', str(v1), str(v2)])
        client_socket.send(testcase.encode())
        oval = float(client_socket.recv(1024).decode())
        print(oval, eval)
        self.assertEqual(eval, oval, FAILURE)

    def test_mul(self):
        v1 = random.randint(1, 100)
        v2 = random.randint(1, 100)
        eval = float(v1 * v2)
        testcase = ','.join(['mul', str(v1), str(v2)])
        client_socket.send(testcase.encode())
        oval = float(client_socket.recv(1024).decode())
        print(oval, eval)
        self.assertEqual(eval, oval, FAILURE)

    def test_div(self):
        v1 = random.randint(1, 100)
        v2 = random.randint(1, 100)
        eval = float(v1 / v2)
        testcase = ','.join(['div', str(v1), str(v2)])
        client_socket.send(testcase.encode())
        oval = float(client_socket.recv(1024).decode())
        print(oval, eval)
        self.assertEqual(eval, oval, FAILURE)

if __name__ == '__main__':


    unittest.main()
    client_socket.close()  # close the connection