import tkinter as tk
from tkinter import PhotoImage
import os

class MenuApp:
    def __init__(self):
        self.menu = tk.Toplevel()
        self.menu.geometry("450x450")
        self.menu.title("Menú principal")
        self.menu.resizable(0, 0)
        
        # Cargar las imágenes para cada botón
        self.image = PhotoImage(file="Images/menu.gif")  # Cambia la ruta de la imagen MENU
        self.image1 = PhotoImage(file="Images/principiante.png")  # Cambia la ruta de la primera imagen
        self.image2 = PhotoImage(file="Images/medio.png")  # Cambia la ruta de la segunda imagen
        self.image3 = PhotoImage(file="Images/dificil.png")  # Cambia la ruta de la tercera imagen
        
        # Crear un widget Label para mostrar la imagen MENU
        self.image_label = tk.Label(self.menu, image=self.image)
        self.image_label.pack()  # Empaqueta el widget en la ventana

        # Añadir los botones con las imágenes correspondientes
        self.button1 = tk.Button(self.menu, command=self.on_button1_click,
                                image=self.image1, compound=tk.TOP)
        self.button1.pack(pady=10, padx=15)

        self.button2 = tk.Button(self.menu, command=self.on_button2_click,
                                image=self.image2, compound=tk.TOP)
        self.button2.pack(pady=20, padx=25)

        self.button3 = tk.Button(self.menu, command=self.on_button3_click,
                                image=self.image3, compound=tk.TOP)
        self.button3.pack(pady=30, padx=35)

        # Se pueden añadir más elementos o funcionalidades aquí
        
        self.menu.mainloop()

    def on_button1_click(self):
        print("Se hizo clic en el botón 1")

    def on_button2_click(self):
        print("Se hizo clic en el botón 2")

    def on_button3_click(self):
        print("Se hizo clic en el botón 3")