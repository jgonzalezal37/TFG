from tkinter import *
from collections import deque
from queue import PriorityQueue, Queue
import random
from PIL import Image, ImageTk
from threading import Thread  # Asumiendo que menu.py contiene la clase MenuApp


class modoPrincipiante:
    def __init__(self):
        self.t = Tk()
        self.t.overrideredirect(1)
        self.t.geometry(f"650x675+{int(self.t.winfo_screenwidth()/2)-325}+40")
        self.t.config(bg="#3b53a0")
        self.t.iconbitmap("Icons/A.ico")
        self.t.title((" " * 80) + "Sliding puzzle")
        self.t.resizable(0, 0)
        self.f = Frame(self.t, bg="#000")
        self.f.place(x=0, y=0, width=600, height=600)
        self.Lab = []
        self.index = 8
        self.b = False
        self.youwin = Label(self.t, image=None)
        self.restart = Label(self.t, image=None)
        self.logo = Label(self.t, image=None)
        self.changetheimage = Label(self.t, image=None)

        # Resto del código de inicialización
        FINAL_STATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.listaFrames = []  # Almacenamos los Frames que representan cada celda del rompecabezas
        self.listaImagenes = []  # Lista de imagenes del rompecabezas, almacena las imagenes que representa cada celda del rompecabezas
        self.listaImagenesCopia = []  # Copia de la lista anterior para que cada vez que manipulemos el orden de las imagenes al deslizar tener un
        # un punto de partida al que poder volver
        self.Lab = []  # Muestra graficamente las imagenes del rompezabezas usando la libreria tkinder (listas de etiquetas)
        self.cmp = 0  # Contador que lleva el numero de piezas creadas en el rompecabezas
        path = "Images/m.png"
        for i in range(3):
            for j in range(3):
                self.listaFrames.append(Frame(self.f))
                if i == 2 and j == 2:
                    self.Lab.append(Label(self.listaFrames[self.cmp], background="#242424"))
                    self.listaImagenes.append(["", self.cmp])
                    self.listaImagenesCopia.append(["", self.cmp])
                else:
                    img = Image.open(path).resize((600, 600)).crop(((j*200), (i*200), ((j*200)+200), ((i*200)+200)))
                    self.listaImagenes.append([ImageTk.PhotoImage(img), self.cmp])
                    self.listaImagenesCopia.append([ImageTk.PhotoImage(img), self.cmp])
                    # Con .crop dividimos la imagen en las partes que queramos
                    self.Lab.append(Label(self.listaFrames[self.cmp], image=self.listaImagenes[self.cmp][0], background="#3b53a0"))
                self.Lab[self.cmp].bind("<Button-1>", lambda event, h=self.cmp: self.lol(event, h))
                self.Lab[self.cmp].place(x=2, y=2, width=196, height=196)
                self.listaFrames[self.cmp].place(x=j*200, y=i*200, width=200, height=200)
                self.cmp += 1

        self.FINAL_STATE = self.listaImagenes

        self.introf = Frame(self.t)
        self.introf.place(x=0, y=0, width=650, height=650)
        self.introi = [ImageTk.PhotoImage(Image.open("Images/1_2.png").resize((300, 300))),
                       ImageTk.PhotoImage(Image.open("Images/2_2.png").resize((300, 300))),
                       ImageTk.PhotoImage(Image.open("Images/3_2.png").resize((300, 300)))]
        self.introl = Label(self.introf, bg="#3b53a0")
        self.introl.place(x=0, y=0, width=650, height=650)

    def lol(self, event, h):
        # h es el numero de la pieza que fue clicada.
        if self.Lab[h].cget("bg") == "#242424" and (h-1 == self.index or h+1 == self.index or h+3 == self.index or h-3 == self.index):
            self.Lab[h].config(image=self.listaImagenesCopia[self.index][0])
            ih = self.listaImagenesCopia[h][1]
            self.listaImagenesCopia[h] = [self.listaImagenesCopia[self.index][0], self.listaImagenesCopia[self.index][1]]  # Intercambia el valor de las dos celdas
            self.listaImagenesCopia[self.index] = ["", ih]
            self.Lab[self.index].config(image="")
            self.Lab[h].config(bg="#3b53a0")  # Nueva celda clicada
            self.Lab[self.index].config(bg="#242424")  # Nueva celda vacia
            print("Estado actual: ")
            print(self.state_to_matrix(self.listaImagenesCopia))
            matriz = self.state_to_matrix(self.listaImagenesCopia)
            print("Pasos hasta la solución: ")
            print(self.solve_puzzle_bfs(matriz))
            listaPrueba = []
            for e in range(len(self.listaImagenesCopia)):
                listaPrueba.append(self.listaImagenesCopia[e][1])

            k = 0
            for i in range(len(self.listaImagenesCopia)):
                for j in range(len(self.listaImagenesCopia[i])):
                    if self.FINAL_STATE[k][1] != listaPrueba[k]:
                        self.b = False
                        k = len(self.listaImagenesCopia)
                        break
                    else:
                        self.b = True
                    k += 1
        self.index = h
        if self.b:
            self.youwin.config(image=self.introi[2])
            self.youwin.place(x=100, y=200, width=450, height=250)
            self.restart.config(image=self.introi[1])
            self.restart.place(x=215, y=500, width=200, height=50)

    def state_to_matrix(self, state):
        matrix = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(state[i * 3 + j][1])
            matrix.append(row)
        return matrix

    def solve_puzzle_bfs(self, start_state):
        start_state = tuple(map(tuple, start_state))
        visited = set()
        queue = Queue()
        queue.put((start_state, []))
        while not queue.empty():
            current_state, path = queue.get()
            if current_state == self.FINAL_STATE:
                return path
            if current_state in visited:
                continue
            visited.add(current_state)
            i, j = next((i, j) for i in range(3) for j in range(3) if current_state[i][j] == 0)
            for move, (di, dj) in enumerate(((0, 1), (1, 0), (0, -1), (-1, 0)), start=1):
                if 0 <= i + di < 3 and 0 <= j + dj < 3:
                    new_state = list(map(list, current_state))
                    new_state[i][j], new_state[i + di][j + dj] = new_state[i + di][j + dj], new_state[i][j]
                    queue.put((tuple(map(tuple, new_state)), path + [move]))
        return None

    def run(self):
        self.t.mainloop()


if __name__ == "__main__":
    app = modoPrincipiante()
    app.run()
