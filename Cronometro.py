# -*- coding: utf-8 -*-
"""
Created on Wed May  6 14:16:44 2020

@author: jdros
"""

from tkinter import *
from tkinter.font import Font

global continuar
continuar=True 

class interfaz:
    def iniciarCronometro(self):
         global continuar
         continuar=True
         self.tick()
    def detenerCronometro(self):
        global continuar
        continuar=False
    def reiniciarCronometro(self):
        global continuar
        continuar= False
        self.text.set("00:00:00")
        self.horas.reinciarValor()
        self.minutos.reinciarValor()
        self.segundos.reinciarValor()
    def tick(self):
        global continuar
        if(continuar):
            self.segundos.aumentarValor()
            if(self.segundos.obtenerValor()==59):
                self.minutos.aumentarValor()
            if(self.minutos.obtenerValor()==59):
                self.horas.aumentarValor()
            resultado=self.horas.obtenerValor()+":"+self.minutos.obtenerValor()+":"+self.segundos.obtenerValor()
            self.text.set(resultado)
        if(continuar):
            self.root.after(930,self.tick)
        
    def  __init__(self,hora,minuto,segundo):
        self.horas=hora
        self.minutos=minuto
        self.segundos=segundo
        self.root=Tk()
        self.root.title("Cronometro")     #Ponerle el nombre a la ventana
        self.root.geometry("350x100")
        self.root.resizable(False,False)
        self.text = StringVar()
        self.text.set("00:00:00")
        self.myFont =Font(family="Times New Roman", size=18)
        self.etiqueta = Label(self.root,textvariable=self.text)
        self.etiqueta.pack()
        self.etiqueta.configure(font=self.myFont)
        self.btnReiniciar = Button(self.root,text="Reiniciar",fg="Blue",command= self.reiniciarCronometro).place(x=10,y=70,height=20,width=80) 
        self.btnIniciar = Button(self.root,text="Iniciar",fg="Green",command= self.iniciarCronometro).place(x=130,y=70,height=20,width=80) 
        self.btnParar = Button(self.root,text="Parar",fg="red",command= self.detenerCronometro).place(x=250,y=70,height=20,width=80)  
    
class Contador:
        valor=0
        limite=0
        def __init__(self,Valor):
            self.limite=Valor
        def aumentarValor(self):
            self.valor +=1
        def obtenerValor(self):
            if(self.valor<10):
                return "0"+str(self.valor)
            else :
                return str(self.valor)
        def reinciarValor(self):
            self.valor=0
class Hora(Contador):
    def __init__(self,Valor):
        Contador.__init__(self,Valor)
    def aumentarValor(self):
        if(self.valor==24):
            self.valor=0
        else:
            self.valor +=1
class Minuto(Contador):
    def __init__(self,Valor):
        Contador.__init__(self,Valor)
    def aumentarValor(self):
        if(self.valor==60):
            self.valor=0
        else:
            self.valor +=1
class Segundo(Contador):
    def __init__(self,Valor):
        Contador.__init__(self,Valor)
    def aumentarValor(self):
        if(self.valor==60):
            self.valor=0
        else:
            self.valor +=1

hora=Hora(24)
minuto=Minuto(60)
segundo= Segundo(60)
App=interfaz(hora,minuto,segundo)
App.root.mainloop()  #Mantiene la ventana abierta