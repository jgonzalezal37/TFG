import tkinter as tk
from tkinter import PhotoImage
import os
from juego import *

class MenuApp:
    def __init__(self):
        self.menu = tk.Toplevel()
        self.menu.geometry("450x400")
        self.menu.title("Menú principal")
        self.menu.resizable(0, 0)
        
        # Cargar las imágenes para cada botón
        self.image = PhotoImage(file="Images/menu.gif")  # Cambia la ruta de la imagen MENU
        self.image1 = PhotoImage(file="Images/principiante.png")  # Cambia la ruta de la primera imagen
        self.image2 = PhotoImage(file="Images/medio.png")  # Cambia la ruta de la segunda imagen
        self.image3 = PhotoImage(file="Images/dificil.png")  # Cambia la ruta de la tercera imagen

        def modoFacil(event):
            modoFacil = modoPrincipiante()
        
        # Crear un widget Label para mostrar la imagen MENU
        self.image_label = tk.Label(self.menu, image=self.image)
        self.image_label.pack()  # Empaqueta el widget en la ventana

        # Añadir los botones con las imágenes correspondientes
        self.principante = tk.Label(self.menu, image=self.image1)
        self.principante.place(x=0, y=100, width=450, height=100)
        self.principante.bind("<Button-1>",modoFacil)

        self.image_label = tk.Label(self.menu, image=self.image2)
        self.image_label.place(x=0, y=200, width=450, height=100)

        self.image_label = tk.Label(self.menu, image=self.image3)
        self.image_label.place(x=0, y=300, width=450, height=100)

        # Se pueden añadir más elementos o funcionalidades aquí
        
        self.menu.mainloop()

    def on_button1_click(self):
        print("Se hizo clic en el botón 1")

    def on_button2_click(self):
        print("Se hizo clic en el botón 2")

    def on_button3_click(self):
        print("Se hizo clic en el botón 3")
    