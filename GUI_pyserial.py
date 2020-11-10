import serial
import time
from tkinter import *


# definindo parâmetros da porta serial
#coloque parâmetros apropriados para o projeto
serial = serial.Serial()
serial.baudrate = 38400
serial.port = 'COM4'
serial.timeout=2

a="vai ser substituido no código"
#**************funções******#
def press(str):
    global a
    serial.write(str.encode())
    # print(serial.readline().decode("ascii"))
    a=serial.readline().decode("ascii")
    return(a)
    print(a)
def serialopen():
    serial.open()
def serialclose():
    serial.close()
def testaserial():
    print(serial)
def savetxt():
    global a
    print(a)
    f= open("guru99.txt","w")
    f.write(a)
    f.close()
    

#***********Criando GUI***************#
menu_inicial=Tk()
menu_inicial.title('PYSERIAL')
menu_inicial.geometry("400x600+900+70")
#*********************criando botões**************#
bon=Button(menu_inicial,text='ON',command=lambda:press("are you there?"),height=4,width=4,
           font='arial 16')
bon.grid(row=0,column=0,sticky=W+E+N+S)

boff=Button(menu_inicial,text='OFF',command=lambda:press('off'),height=4,width=4,
           font='arial 16')
boff.grid(row=0,column=1,sticky=W+E+N+S)

bopen=Button(menu_inicial,text='OPEN',command=serialopen,height=4,width=4,
           font='arial 16')
bopen.grid(row=1,column=0,sticky=W+E+N+S)

bclose=Button(menu_inicial,text='CLOSE',command=serialclose,height=4,width=4,
           font='arial 16')
bclose.grid(row=1,column=1,sticky=W+E+N+S)


#apagar depois
btesta=Button(menu_inicial,text='TESTA',command=testaserial,
           font='arial 16')
btesta.grid(row=2,column=0,sticky=W+E+N+S)

bsavetxtx=Button(menu_inicial,text='salvar txt',command=savetxt,
           font='arial 16')
bsavetxtx.grid(row=2,column=1,sticky=W+E+N+S)

menu_inicial.mainloop()




#REFERÊNCIA
#https://pythonhosted.org/pyserial/shortintro.html?highlight=readline