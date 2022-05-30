from distutils.command.config import config
from logging import root
from struct import pack
from tabnanny import check
import tkinter as tk
from tkinter import *
from turtle import color
import time
import threading
import serial

root = tk.Tk()
root.title("Segunda Entrega")
root.resizable(height=False, width=False)


lowerLimitValue = 150
upperLimitValue = 0
sensor = 0
x = 0
y = 150
xa = 0
ya = 0


def timer():
    global sensor
    global x
    global upperLimitValue
    global lowerLimit
    while True:
        nucleo = serial.Serial('COM3', 115200)
        rawString = str(nucleo.readline())
        rawString = rawString.strip("b'\.n")  # Ya tengo mi valor @num# limpio
        # Se verifica la trama
        if(rawString.count('@') == 1) and (rawString.count('#') == 1):
            sensor = int(rawString.strip("@#"))

        x += 1
        if x <= 400:
            y = 150-sensor*3/5
        else:
            x = 0

        transferencia(x, y)

        if sensor < int(lowerLimitValue*-5/3+250):
            nucleo.write(b'a')
        if sensor > int(upperLimitValue*-5/3+250):
            nucleo.write(b'b')
        if sensor > int(lowerLimitValue*-5/3+250) and sensor < int(upperLimitValue*-5/3+250):
            nucleo.write(b'c')

        print(sensor)
        nucleo.close()

        time.sleep(0.1)   # 100 ms


t = threading.Thread(target=timer)
t.start()


def transferencia(vx, vy):
    global xa
    global ya
    global x
    global y
    xa = x
    ya = y
    x = vx
    y = vy
    if xa > x:
        xa = 0
    graphicFrame.create_line(xa, ya, x+1, y, fill="Yellow")
    if ya == y:
        graphicFrame.create_line(xa-1, ya, x, y, fill="Yellow", width=2)
    if x == 400:
        drawPlane()


def start():
    drawPlane()


def drawPlane():
    global lowerLimitValue
    global upperLimitValue

    graphicFrame.delete('all')
    # eje de tiempo
    graphicFrame.create_line(0, 150, 402, 150, fill="White")
    # pilots
    for i in range(30, 300, 30):
        graphicFrame.create_line(0, i, 5, i, fill="White")
    # Limites de la grafica
    graphicFrame.create_line(0, upperLimitValue, 402,
                             upperLimitValue, fill="Red")
    graphicFrame.create_line(0, lowerLimitValue, 402,
                             lowerLimitValue, fill="Purple")


def assignUpperLimit():
    global upperLimitValue
    global x
    upperLimitValue = (int(upperLimit.get())*-3/5)+150
    graphicFrame.delete('all')
    drawPlane()
    x = 0


def assignLowerLimit():
    global lowerLimitValue
    global x
    lowerLimitValue = (int(lowerLimit.get())*-3/5)+150
    graphicFrame.delete('all')
    drawPlane()
    x = 0


# ------------------------Configuracion inicial de frames -------
graphicFrame = tk.Canvas(root, width=400, height=300, bg="Black")
graphicFrame.grid(row=0, column=0)
inputFrame = tk.Canvas(root, width=130, height=300, bg="#f0f0f0")
inputFrame.grid(row=0, column=1, rowspan=2)

# ------------------------Configuracion inicial de frames -------
upperLimit = IntVar()
lowerLimit = IntVar()

tk.Label(inputFrame, text='Limite superior').grid(row=0, column=0, pady=10)
entryUpperLimit = Entry(inputFrame, textvariable=upperLimit)
entryUpperLimit.grid(row=1, column=0, padx=10, pady=10, columnspan=4)
entryUpperLimit.config(background="black", fg="#24F40B", justify="center")
buttonUpperLimit = Button(inputFrame, text="Asignar Superior", command=assignUpperLimit).grid(
    row=2, column=0, padx=10, pady=10)

tk.Label(inputFrame, text='-------------------------').grid(row=3, padx=10, pady=20)

tk.Label(inputFrame, text='Limite inferior').grid(row=4, pady=2,)
entryLowerLimit = Entry(inputFrame, textvariable=lowerLimit)
entryLowerLimit.grid(row=5, column=0, padx=10, pady=10, columnspan=4)
entryLowerLimit.config(background="black", fg="#24F40B", justify="center")
buttonUpperLimit = Button(inputFrame, text="Asignar Inferior", command=assignLowerLimit).grid(
    row=6, column=0, padx=10, pady=10)

start()
root.mainloop()