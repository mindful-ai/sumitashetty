import serial
import time
arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

def read():
    data = arduino.readline()
    print(data)
    return data

def write(x):
    arduino.write(bytes(x, 'utf-8'))
    #time.sleep(0.05)

while True:
    num = input("Enter a number: ") # Taking input from user
    write(num)

    value = arduino.readline()
    print(value) # printing the value