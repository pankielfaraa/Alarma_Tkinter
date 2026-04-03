import tkinter as tk 
from tkinter import ttk, messagebox
import time

#Ventana 

ventana = tk.Tk()
ventana.config(bg="black")
ventana.title("Alarma")
ventana.geometry("500x400")
ventana.resizable(False,False)

estado_alarma = False

frame_principal = tk.Frame(ventana,bg="Black")
frame_principal.pack(expand=True)


frame_uno = tk.Label(frame_principal,text="00:00:00",font=("console",55,"bold"),bg="Black",fg="White")
frame_uno.pack(pady=(15,15))

frame_dos = tk.Entry(frame_principal,text="HH:MM:SS",justify="center",font=("Segoe UI",20),bg="White")
frame_dos.pack(pady=(5,0))
frame_dos.insert(0,"00:00:00")

frame_tres = tk.Label(frame_principal,text="",font=("Segoe UI",30,"bold"),fg="red",bg="black")
frame_tres.pack(pady=(20,0))



def reloj():

    hora_actual = time.strftime("%H:%M:%S")
    frame_uno.config(text=hora_actual)
    ventana.after(1000,reloj)


def activar():
    frame_tres.config(text="Alarma Activa",font=("Segoe UI",30,"bold"),fg="Green",bg="black")

    global estado_alarma
    estado_alarma = True

    comprobar()

def comprobar():
    
    global estado_alarma

    if estado_alarma:
        hora_actual = time.strftime("%H:%M:%S")
        hora_alarma = frame_dos.get()

        if hora_actual == hora_alarma:
            messagebox.showinfo("Alarma", "⏰ ¡Hora cumplida!")
            estado_alarma = False
            frame_tres.config(text="Alarma Inactiva", fg="Red")

        else:
            ventana.after(1000, comprobar)



def Desactivar():
    frame_tres.config(text="Alarma Desactivada",font=("Segoe UI",30,"bold"),fg="Red",bg="black")

    global estado_alarma 
    estado_alarma = False




frame_secundario = tk.Frame(ventana,bg="Black")
frame_secundario.pack(expand=True,anchor="n")


frame_cuatro = tk.Button(frame_secundario,text="Activar",command=activar,font=("Segoe UI",15,"bold"),width=10,bg="Green",fg="White",relief="flat")
frame_cuatro.grid(row=0,column=0,padx=15)

frame_cinco = tk.Button(frame_secundario,text="Desactivar",command=Desactivar,font=("Segoe UI",15,"bold"),width=10,bg="Red",fg="White",relief="flat")
frame_cinco.grid(row=0,column=1,padx=15)







reloj()
ventana.mainloop()