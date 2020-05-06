from tkinter import *
from tkinter.font import Font



class interfaz:
    
    def  __init__(self, root):
        root.title("Cronometro")     #Ponerle el nombre a la ventana
        root.geometry("350x100")
        myFont =Font(family="Times New Roman", size=18)
        etiqueta = Label(root,text="00:00:00")
        etiqueta.pack()
        etiqueta.configure(font=myFont)
        btnReiniciar = Button(root,text="Reiniciar",fg="Blue",command= self.reiniciarCronometro).place(x=10,y=70,height=20,width=80) 
        btnIniciar = Button(root,text="Iniciar",fg="Green",command= self.iniciarCronometro).place(x=130,y=70,height=20,width=80) 
        btnParar = Button(root,text="Parar",fg="red",command= self.detenerCronometro).place(x=250,y=70,height=20,width=80)  
    
    def iniciarCronometro(self):
        print("Se ha inciado el cronometro")
    def detenerCronometro(self):
        print("Se ha detenido el cronometro el cronometro")
    def reiniciarCronometro(self):
        print("Se ha reinciado el cronometro")


ventana= Tk()       #Iniciar la ventana
App=interfaz(ventana)
ventana.mainloop()  #Mantiene la ventana abierta