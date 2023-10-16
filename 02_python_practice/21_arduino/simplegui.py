from tkinter import *
import serial
import time
arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)

class MyWindow:

    def __init__(self, win):

        # Create all the widgets
        self.lbl1=Label(win, text='Number to Send')
        self.lbl2=Label(win, text='Number Received')

        self.t1=Entry(win, bd=3)
        self.t2=Entry(win, bd=3)

        # Attach functionality to all widgets
        self.b1=Button(win, text='Send', command=self.write) # Event Binding
        self.b2=Button(win, text='Receive')
        self.b2.bind('<Button-1>', self.read) # Event Binding

        # Place all the widgets
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)


    def write(self):
        arduino.write(bytes(self.t1.get(), 'utf-8'))


    def read(self, event):
        data = arduino.readline()
        self.t2.insert(END, str(data))

# --------------------------------------------------------------

window=Tk()

mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("800x300+10+10")
window.mainloop()

