from tkinter import *

from collections import deque
from queue import PriorityQueue, Queue
import random
from PIL import Image, ImageTk
from threading import Thread 
from win32api import GetSystemMetrics
from PIL import Image,ImageTk 
from threading import Thread
from time import sleep
from tkinter import messagebox 
from tkinter import filedialog
from menu import *  

class modoPrincipiante:
    FINAL_STATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    def __init__(self):
        self.easyMode = Toplevel()
        self.easyMode.geometry(f"650x675+{int(GetSystemMetrics(0)/2)-325}+40")
        self.easyMode.title((" "*80)+"Modo Fácil") 
        self.easyMode.resizable(0, 0)
        
        self.f = Frame(self.easyMode, bg = "#000")
        self.f.place(x=0,y=0,width=600,height=600)
        
        self.listaFrames = []
        self.listaImagenes = []
        self.listaImagenesCopia = []

        self.Lab = []
        self.cmp = 0
        self.path="Images/m.png" 
        for i in range(3): 
            for j in range(3): 
                self.listaFrames.append(Frame(self.easyMode)) 
                if i==2 and j==2: 
                    self.Lab.append(Label(self.listaFrames[self.cmp],background="#242424")) 
                    self.listaImagenes.append(["",self.cmp]) 
                    self.listaImagenesCopia.append(["",self.cmp]) 
                else: 
                    self.listaImagenes.append([ImageTk.PhotoImage(Image.open(self.path).resize((600,600)).crop(((j*200),(i*200),((j*200)+200),((i*200)+200)))),self.cmp]) 
                    self.listaImagenesCopia.append([ImageTk.PhotoImage(Image.open(self.path).resize((600,600)).crop(((j*200),(i*200),((j*200)+200),((i*200)+200)))),self.cmp])
                    #Con .crop dividimos la imagen en las partes que queramos
                    self.Lab.append(Label(self.listaFrames[self.cmp],image=self.listaImagenes[self.cmp][0],background="#3b53a0")) 
                self.Lab[self.cmp].bind("<Button-1>",lambda event,h=self.cmp:lol(self,event,h)) 
                self.Lab[self.cmp].place(x=2,y=2,width=196,height=196) 
                self.listaFrames[self.cmp].place(x=j*200,y=i*200,width=200,height=200) 
                self.cmp+=1


        self.FINAL_STATE = self.listaImagenes
        self.index=8 


        def lol(self,event,h): 
        #h es el numero de la pieza que fue clicada.
            global b
            if self.Lab[h].cget("bg")=="#242424" and (h-1==self.index or h+1==self.index or h+3==self.index or h-3==self.index) : 
                self.Lab[h].config(image=self.listaImagenesCopia[self.index][0]) 
                self.ih=self.listaImagenesCopia[h][1]
                self.listaImagenesCopia[h]=[self.listaImagenesCopia[self.index][0],self.listaImagenesCopia[self.index][1]] #Intercambia el valor de las dos celdas
                self.listaImagenesCopia[self.index]=["",self.ih] 
                #print(index)
                #index indica el indice donde se encuentra la celda vacia
                self.Lab[self.index].config(image="") 
                self.Lab[h].config(bg="#3b53a0") #Nueva celda clicada
                self.Lab[self.index].config(bg="#242424") #Nueva celda vacia
                print("Estado actual: ")
                print(state_to_matrix(self.listaImagenesCopia))
                matriz = state_to_matrix(self.listaImagenesCopia)
                print("Pasos hasta la solución: ")
                print(solve_puzzle_bfs(matriz))
                self.listaPrueba = []
                for e in range(len(self.listaImagenesCopia)):
                    self.listaPrueba.append(self.listaImagenesCopia[e][1])
                # estado_inicial = generate_initial_state(self.listaPrueba)
                # print(estado_inicial)
                # print("SOLUCION: ")
                # print(solve_puzzle_bfs(matriz))
        
                k=0 
                for i in range(len(self.listaImagenesCopia)): 
                    if self.listaImagenesCopia[i][1]==self.listaImagenes[i][1]: #Comparamos 1 a 1 los identificadores de las dos listas
                        k+=1 
                if k==(len(self.listaImagenesCopia)): #Cuando se cumple este if todos los identificadores de las dos listas coinciden
                    #por lo que habremos llegado a la solucion
                    changetheimage.place_forget() 
                    youwin.place(x=0,y=600,width=500,height=50) 
                    b=False 
                    Thread(target=lambda y=youwin:tim(y)).start() 
            self.listaFrames[self.index].config(bg="white") 
            self.index=h 
            self.listaFrames[h].config(bg="black")

        def tim(youwin): 
            w=0 
            while True: 
                try: 
                    if w%2 == 0: 
                        youwin.config(image=yww) 
                    else: 
                        youwin.config(image=yw)
                    w+=1 
                    if w==100: 
                        w=0 
                    sleep(0.5) 
                    if b: 
                        return 
                except: 
                    return
                
        def ayuda(event):
            matriz = state_to_matrix(self.listaImagenesCopia)
            pasos = solve_puzzle_bfs(matriz)
            if pasos == 1:
                messagebox.askokcancel("", "Estás a un paso de llegar a la solución.")
            elif pasos == 0:
                messagebox.askokcancel("", "¡Has llegado a la solución!")
            else:
                messagebox.askokcancel("", "Estás a "+ str(pasos)+ " pasos de llegar a la solución.")

        def menu(event):
            menu = MenuApp()

        def modoFacil(event):
            app = modoPrincipiante()

        def cticlick(event): 
            filetypes = ( 
                        ('Images', '*.png'), 
                        ('All files', '*.png')
                        )
            self.easyMode.iconbitmap("Icons/A.ico") 
            e =filedialog.askopenfile(title='Open the image (with the same dimensions)', 
                                    initialdir='/', 
                                    filetypes=filetypes)
            #if e!=None: 

            if e is not None:
                img = Image.open(e.name)
                if img.width != img.height:
                    #t.withdraw() #Oculta la ventana principal
                    # Si las dimensiones no coinciden, abrir una ventana de vista previa y permitir al usuario ajustarlas
                    #new_width = simpledialog.askinteger("Adjust Image Dimensions", "Width (pixels):", initialvalue=img.width)
                    #new_height = simpledialog.askinteger("Adjust Image Dimensions", "Height (pixels):", initialvalue=img.height)
                    #t.deiconify() #Muestra la ventana principal
                    img = img.resize((650, 650), Image.ANTIALIAS)
                    #img.save(e.name)  # Guardar la imagen con las nuevas dimensiones  
                path=e.name 
                self.listaImagenes.clear() 
                self.listaImagenesCopia.clear() 
                self.easyMode.title((" "*60)+"Modo Fácil | The image is loading ...") 
                cmp=0 
                for i in range(3): 
                    for j in range(3): 
                        if i==2 and j==2: 
                                self.listaImagenes.append(["",cmp]) 
                                self.listaImagenesCopia.append(["",cmp]) 
                        else: 
                                self.listaImagenes.append([ImageTk.PhotoImage(Image.open(path).resize((600,600)).crop(((j*200),(i*200),((j*200)+200),((i*200)+200)))),cmp]) 
                                self.listaImagenesCopia.append([ImageTk.PhotoImage(Image.open(path).resize((600,600)).crop(((j*200),(i*200),((j*200)+200),((i*200)+200)))),cmp]) 
                        cmp+=1
            cos(None)
            self.easyMode.title((" "*80)+"Modo Fácil") 
            self.easyMode.iconbitmap("Icons/A.ico")

        def cos(event): 
            global b 
            if event: 
                #shuffle(listaImagenesCopia)
                self.listaImagenesCopia = apply_random_moves(self.listaImagenesCopia)
                self.listaImagenesCopia = apply_random_moves(self.listaImagenesCopia)
                #listaImagenesCopia = generate_initial_state(FINAL_STATE) #Ahora mismo generamos el tablero de manera aleatoria con shuffle, tenemos que implementar
            #el algoritmo de backtracking y generar a partir de dicho algoritmo el tablero.
                # print("LISTA IMAGENES COPIA: ")
                # print(listaImagenesCopia)
                # print(state_to_matrix(listaImagenesCopia))
            for i in range(len(self.listaImagenesCopia)): 
                self.Lab[i].config(image=self.listaImagenesCopia[i][0]) 
                self.Lab[i].config(bg="#3b53a0") 
            for j in range(len(self.listaImagenesCopia)): 
                if self.listaImagenesCopia[j][0]=="": 
                    self.Lab[j].config(bg="#242424") 
            b=True 
            youwin.place_forget() 
            changetheimage.place(x=0,y=600,width=500,height=50)

        def apply_random_moves(current_state):
            """
            Realiza 100 movimientos aleatorios en el juego utilizando la función lol.

            Parameters:
                current_state (list): El estado actual del juego representado como una lista.

            Returns:
                list: El estado actualizado del juego después de realizar los movimientos aleatorios.
            """
            for _ in range(100):
                # Selecciona una celda aleatoria para realizar un movimiento
                cell = random.randint(0, 8)
                # Simula un clic en la celda seleccionada
                lol(self,None, cell)
            
            # Devuelve el estado actualizado después de los movimientos aleatorios
            return current_state
        
        def state_to_matrix(listaImagenesCopia):
            # Convertir listaImagenesCopia a una matriz de 4x4
            matrix = [[0] * 3 for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    matrix[i][j] = listaImagenesCopia[i * 3 + j][1]
            return matrix
        
        def is_goal(state):
            final_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
            return state == final_state
    
        def heuristic(state):
            goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
            total_cost = 0
            for i in range(3):
                for j in range(3):
                    if state[i][j] != 0:
                        row = (state[i][j] - 1) // 3 # (fila 0, 1 o 2) Calcular fila objetivo
                        col = (state[i][j] - 1) % 3 # (resto 0, 1 o 2) Calcular columna objetivo
                        total_cost += abs(i - row) + abs(j - col) # Sumamos la distancia desde (i,j) hasta (row,col)
            return total_cost
        
        def generate_successors(state):
            successors = []
            # Encontrar la posición de la casilla vacía
            empty_row, empty_col = -1, -1
            for i in range(3):
                for j in range(3):
                    if state[i][j] == 8:
                        empty_row, empty_col = i, j
                        break
            # Mover la casilla vacía hacia arriba, abajo, izquierda y derecha si es posible
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = empty_row + dr, empty_col + dc
                if 0 <= new_row < 3 and 0 <= new_col < 3:
                    new_state = [row[:] for row in state]  # Copiar el estado actual
                    new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]  # Intercambiar casillas
                    successors.append(new_state)
            return successors
        
        def solve_puzzle_bfs(initial_state):
            # Conjunto para almacenar los estados visitados
            visited = set()
            # Cola para almacenar los estados por explorar
            q = Queue()
            # Contador de pasos tomados
            steps_taken = 0
            # Número máximo de pasos permitidos
            max_steps = 10000000000
            
            # Agregar el estado inicial a la cola
            q.put((0, initial_state))  # Tupla: (pasos restantes, estado actual)
            
            # Bucle principal
            while not q.empty() and steps_taken < max_steps:
                # Obtener el estado de la cola
                steps, state = q.get()
                
                # Comprobar si se ha alcanzado el estado objetivo
                if state == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
                    return steps  # Devolver el número de pasos tomados
                
                # Comprobar si el estado no ha sido visitado previamente
                if tuple(map(tuple, state)) not in visited:
                    # Agregar el estado actual al conjunto de estados visitados
                    visited.add(tuple(map(tuple, state)))
                    
                    # Generar sucesores del estado actual
                    for successor in generate_successors(state):
                        # Agregar el sucesor a la cola con los pasos restantes
                        q.put((steps + 1, successor))
                        
                # Incrementar el contador de pasos tomados
                steps_taken += 1
            
            # Si se excede el número máximo de pasos permitidos o la cola está vacía, retornar None
            return None

        

        yw=ImageTk.PhotoImage((Image.open("Images/ganador1.png"))) 
        yww=ImageTk.PhotoImage((Image.open("Images/ganador2.png"))) 
        youwin=Label(self.easyMode,image=yw)

        cti=ImageTk.PhotoImage((Image.open("Images/changeImg.png"))) 
        ctiw=ImageTk.PhotoImage((Image.open("Images/changeImg2.png"))) 
        changetheimage=Label(self.easyMode,image=cti) 
        changetheimage.place(x=0,y=600,width=500,height=50) 
        changetheimage.bind("<Enter>",lambda event:changetheimage.config(image=ctiw)) 
        changetheimage.bind("<Leave>",lambda event:changetheimage.config(image=cti))
        changetheimage.bind("<Button-1>",cticlick)

        iim=ImageTk.PhotoImage((Image.open("Images/GameOn.png"))) 
        iimw=ImageTk.PhotoImage((Image.open("Images/GameOn2.png"))) 
        restart=Label(self.easyMode,image=iim) 
        restart.place(x=600,y=0,width=50,height=600) 
        restart.bind("<Enter>",lambda event:restart.config(image=iimw)) 
        restart.bind("<Leave>",lambda event:restart.config(image=iim))
        restart.bind("<Button-1>",cos)
        
        _logo=ImageTk.PhotoImage((Image.open("Images/ayuda.png"))) 
        logo=Label(self.easyMode,image=_logo) 
        logo.place(x=600,y=600,width=50,height=50)

        logo.bind("<Button-1>",ayuda)
        menuImg=ImageTk.PhotoImage((Image.open("Images/menu2.gif")))
        menuLog=Label(self.easyMode,image=menuImg)
        menuLog.place(x=500, y=600, width=100, height=50)
        menuLog.bind("<Button-1>",menu)

        
    

     
        

        self.easyMode.mainloop()

    def modoFacil(self, event):
        modoFacil = modoPrincipiante()
        modoFacil.run()