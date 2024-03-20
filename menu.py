import tkinter as tk
from tkinter import PhotoImage
import os
from modoFacil import modoPrincipiante
from modoMedio import modoMedio

class MenuApp:
    def __init__(self):
        self.menu = tk.Toplevel()
        self.menu.geometry("450x400")
        self.menu.title("Menú principal")
        self.menu.resizable(0, 0)
        
        # Cargar las imágenes para cada botón
        self.image = PhotoImage(file="Images/menu.gif")
        self.image1 = PhotoImage(file="Images/principiante.png")
        self.image2 = PhotoImage(file="Images/medio.png")
        self.image3 = PhotoImage(file="Images/dificil.png")

        # Crear un widget Label para mostrar la imagen MENU
        self.image_label = tk.Label(self.menu, image=self.image)
        self.image_label.pack()

        # Añadir los botones con las imágenes correspondientes
        self.principiante = tk.Label(self.menu, image=self.image1)
        self.principiante.place(x=0, y=100, width=450, height=100)
        self.principiante.bind("<Button-1>", self.modoFacil)

        self.medio = tk.Label(self.menu, image=self.image2)
        self.medio.place(x=0, y=200, width=450, height=100)
        self.medio.bind("<Button-1>", self.nivelMedio)

        self.image_label = tk.Label(self.menu, image=self.image3)
        self.image_label.place(x=0, y=300, width=450, height=100)

        self.menu.mainloop()

    def modoFacil(self, event):
        modoFacil = modoPrincipiante()
        modoFacil.run()

    def nivelMedio(self, event):
        nivelMedio = modoMedio()
        nivelMedio.run()

