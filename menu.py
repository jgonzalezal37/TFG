import tkinter as tk

class MenuApp:
    def __init__(self):
        self.menu = tk.Toplevel()
        self.menu.geometry("450x450")
        self.menu.title("Menú principal")
        self.menu.resizable(0, 0)
        self.menu.iconbitmap("Icons/A.ico")
        self.image = tk.PhotoImage(file="Images/slice_game.png")
        #self.image2 = tk.PhotoImage(file="Images/slice_game.png")
        self.image_label = tk.Label(self.menu, image=self.image)
        #self.image_label2 = tk.Label(self.menu, image=self.image2)
        self.image_label.place(x=0,y=0,width=450,height=100)
        #self.image_label2.place(x=0,y=100,width=450,height=100)
        
        self.menu.mainloop()