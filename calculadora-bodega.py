import customtkinter as ctk

ctk.set_appearance_mode("ligth")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

ventana = ctk.CTk()  # create CTk window like you do with the Tk window
ventana.title("Calculadora simple")

anchoInt, altoInt = 450, 550
ancho, alto = str(anchoInt), str(altoInt)
dimensiones = ancho + "x" + alto
posicion = "+350+100"
ventana.geometry(dimensiones+posicion)

def escribir_num(num):
    entry.insert(ctk.END, str(num))
    print(entry.get())

def borrar():
    entry.delete(0, ctk.END)

def resultado():
    resultado = eval(entry.get())
    entry.insert(ctk.END, str("="))
    out.delete(0, ctk.END)
    out.insert(ctk.END, resultado)
    print(resultado)

entry = ctk.CTkEntry(ventana, width=440, height=50, font=("Arial",25) )
entry.place_configure(relx=0.5, rely=0.5, anchor=ctk.CENTER)
entry.pack()

out = ctk.CTkEntry(ventana, width=440, height=125, font=("Arial",50) )
out.place_configure(relx=0.5, rely=0.8, anchor=ctk.CENTER)
out.pack()

# Configuracion de boton
anchoBoton = 100
altoBoton = 80
letraBoton = ("Arial", 54)

boton_AC = ctk.CTkButton(ventana, text="AC", command=lambda:borrar(), width=anchoBoton, height=altoBoton, font=letraBoton)
boton_AC.place(relx = (1/8), rely = (1/3+1/12), anchor=ctk.CENTER)

boton_entre = ctk.CTkButton(ventana, text="/", command=lambda:escribir_num("/"), width=anchoBoton, height=altoBoton, font=letraBoton)
boton_entre.place(relx = (3/8), rely = (1/3+1/12), anchor=ctk.CENTER)

boton_por = ctk.CTkButton(ventana, text="*", command=lambda: escribir_num("*"), width=anchoBoton, height=altoBoton, font=letraBoton)
boton_por.place(relx = (5/8), rely = (1/3+1/12), anchor=ctk.CENTER)

boton_menos = ctk.CTkButton(ventana, text="-", command=lambda:escribir_num("-"), width=anchoBoton, height=altoBoton, font=letraBoton)
boton_menos.place(relx = (7/8), rely = (1/3+1/12), anchor=ctk.CENTER)

####################################

boton7 = ctk.CTkButton(ventana, text="7", command=lambda:escribir_num(7), width=anchoBoton, height=altoBoton, font=letraBoton)
boton7.place(relx = (1/8), rely = (1/3+3/12), anchor=ctk.CENTER)

boton8 = ctk.CTkButton(ventana, text="8", command=lambda: escribir_num(8), width=anchoBoton, height=altoBoton, font=letraBoton)
boton8.place(relx = (3/8), rely = (1/3+3/12), anchor=ctk.CENTER)

boton9 = ctk.CTkButton(ventana, text="9", command=lambda:escribir_num(9), width=anchoBoton, height=altoBoton, font=letraBoton)
boton9.place(relx = (5/8), rely = (1/3+3/12), anchor=ctk.CENTER)

boton_mas = ctk.CTkButton(ventana, text="+", command=lambda:escribir_num("+"), width=anchoBoton, height=altoBoton, font=letraBoton)
boton_mas.place(relx = (7/8), rely = (1/3+3/12), anchor=ctk.CENTER)

####################################

boton4 = ctk.CTkButton(ventana, text="4", command=lambda:escribir_num(4), width=anchoBoton, height=altoBoton, font=letraBoton)
boton4.place(relx = (1/8), rely = (1/3+5/12), anchor=ctk.CENTER)

boton5 = ctk.CTkButton(ventana, text="5", command=lambda:escribir_num(5), width=anchoBoton, height=altoBoton, font=letraBoton)
boton5.place(relx = (3/8), rely = (1/3+5/12), anchor=ctk.CENTER)

boton6 = ctk.CTkButton(ventana, text="6", command=lambda: escribir_num(6), width=anchoBoton, height=altoBoton, font=letraBoton)
boton6.place(relx = (5/8), rely = (1/3+5/12), anchor=ctk.CENTER)

boton_punto = ctk.CTkButton(ventana, text="=", command=lambda:resultado(), width=anchoBoton, height=altoBoton, font=letraBoton)
boton_punto.place(relx = (7/8), rely = (1/3+5/12), anchor=ctk.CENTER)

####################################

boton1 = ctk.CTkButton(ventana, text="1", command=lambda:escribir_num(1), width=anchoBoton, height=altoBoton, font=letraBoton)
boton1.place(relx = (1/8), rely = (1/3+7/12), anchor=ctk.CENTER)

boton2 = ctk.CTkButton(ventana, text="2", command=lambda:escribir_num(2), width=anchoBoton, height=altoBoton, font=letraBoton)
boton2.place(relx = (3/8), rely = (1/3+7/12), anchor=ctk.CENTER)

boton3 = ctk.CTkButton(ventana, text="3", command=lambda: escribir_num(3), width=anchoBoton, height=altoBoton, font=letraBoton)
boton3.place(relx = (5/8), rely = (1/3+7/12), anchor=ctk.CENTER)

boton0 = ctk.CTkButton(ventana, text="0", command=lambda:escribir_num(0), width=anchoBoton, height=altoBoton, font=letraBoton)
boton0.place(relx = (7/8), rely = (1/3+7/12), anchor=ctk.CENTER)

####################################

ventana.mainloop()