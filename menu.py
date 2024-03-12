import tkinter as tk

class MenuApp:
    def __init__(self, root):
        self.root = root
        self.create_menu()

    def do_something(self):
        print("Se ha seleccionado una opción del menú.")

    def exit_app(self):
        self.root.destroy()

    def create_menu(self):
        # Crear el menú
        menu_bar = tk.Menu(self.root)

        # Menú Archivo
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Abrir", command=self.do_something)
        file_menu.add_command(label="Guardar", command=self.do_something)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.exit_app)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)

        # Menú Ayuda
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Ayuda", command=self.do_something)
        help_menu.add_separator()
        help_menu.add_command(label="Acerca de", command=self.do_something)
        menu_bar.add_cascade(label="Ayuda", menu=help_menu)

        # Configurar la ventana principal para usar el menú
        self.root.config(menu=menu_bar)

