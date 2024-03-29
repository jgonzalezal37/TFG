from tkinter import * 
from collections import deque
from queue import PriorityQueue
from random import random
FINAL_STATE = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
t=Tk() 
t.overrideredirect(1)
from win32api import GetSystemMetrics 
t.geometry(f"650x675+{int(GetSystemMetrics(0)/2)-325}+40") 
t.config(bg="#3b53a0") 
t.iconbitmap("Icons/w.ico") 
t.title((" "*80)+"Sliding puzzle") 
t.resizable(0,0) 
f=Frame(t,bg="#000") 
f.place(x=0,y=0,width=600,height=600) 
listaFrames=[] #Almacenamos los Frames que representan cada celda del rompecabezas
listaImagenes=[] #Lista de imagenes del rompecabezas, almacena las  imagenes que representa cada celda del rompecabezas
listaImagenesCopia=[] #Copia de la lista anterior para que cada vez que manipulemos el orden de las imagenes al deslizar tener un
       #un punto de partida al que poder volver
Lab=[] #Muestra graficamente las imagenes del rompezabezas usando la libreria tkinder (listas de etiquetas)
cmp=0 #Contador que lleva el numero de piezas creadas en el rompecabezas
from PIL import Image,ImageTk 
path="Images/m.png" 
for i in range(4): 
    for j in range(4): 
        listaFrames.append(Frame(f)) 
        if i==3 and j==3: 
            Lab.append(Label(listaFrames[cmp],background="#242424")) 
            listaImagenes.append(["",cmp]) 
            listaImagenesCopia.append(["",cmp]) 
        else: 
            listaImagenes.append([ImageTk.PhotoImage(Image.open(path).resize((600,600)).crop(((j*150),(i*150),((j*150)+150),((i*150)+150)))),cmp]) 
            listaImagenesCopia.append([ImageTk.PhotoImage(Image.open(path).resize((600,600)).crop(((j*150),(i*150),((j*150)+150),((i*150)+150)))),cmp])
            #Con .crop dividimos la imagen en las partes que queramos
            Lab.append(Label(listaFrames[cmp],image=listaImagenes[cmp][0],background="#3b53a0")) 
        Lab[cmp].bind("<Button-1>",lambda event,h=cmp:lol(event,h)) 
        Lab[cmp].place(x=2,y=2,width=147,height=147) 
        listaFrames[cmp].place(x=j*150,y=i*150,width=150,height=150) 
        cmp+=1 
index=15 
from threading import Thread 
def lol(event,h): 
    #h es el numero de la pieza que fue clicada.
    global index,t,b 
    if Lab[h].cget("bg")=="#242424" and (h-1==index or h+1==index or h+4==index or h-4==index) : 
        Lab[h].config(image=listaImagenesCopia[index][0]) 
        ih=listaImagenesCopia[h][1]
        listaImagenesCopia[h]=[listaImagenesCopia[index][0],listaImagenesCopia[index][1]] #Intercambia el valor de las dos celdas
        listaImagenesCopia[index]=["",ih] 
        #print(index)
        #index indica el indice donde se encuentra la celda vacia
        Lab[index].config(image="") 
        Lab[h].config(bg="#3b53a0") #Nueva celda clicada
        Lab[index].config(bg="#242424") #Nueva celda vacia
        matriz = state_to_matrix(listaImagenesCopia)
        print("SOLUCION: ")
        print(solve_puzzle_a_star(matriz))
        k=0 
        for i in range(len(listaImagenesCopia)): 
            if listaImagenesCopia[i][1]==listaImagenes[i][1]: #Comparamos 1 a 1 los identificadores de las dos listas
                k+=1 
        if k==(len(listaImagenesCopia)): #Cuando se cumple este if todos los identificadores de las dos listas coinciden
            #por lo que habremos llegado a la solucion
            changetheimage.place_forget() 
            youwin.place(x=0,y=600,width=600,height=50) 
            b=False 
            Thread(target=lambda y=youwin:tim(y)).start() 
    listaFrames[index].config(bg="white") 
    index=h 
    listaFrames[h].config(bg="black")
    
yw=ImageTk.PhotoImage((Image.open("Images/youwin.png"))) 
yww=ImageTk.PhotoImage((Image.open("Images/youwinwhite.png"))) 
youwin=Label(t,image=yw) 
from time import sleep 
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
iim=ImageTk.PhotoImage((Image.open("Images/restart.png"))) 
iimw=ImageTk.PhotoImage((Image.open("Images/restartwhite.png"))) 
restart=Label(t,image=iim) 
restart.place(x=600,y=0,width=50,height=600) 
restart.bind("<Enter>",lambda event:restart.config(image=iimw)) 
restart.bind("<Leave>",lambda event:restart.config(image=iim))
#Con el comando enter y leave dentro del bind lo que hacemos esque cuando el cursor entra en la imagen se selecciona
#la imagen iimw y cuando sale se selecciona la imagen iim, asi creamos un efecto de hover sobre la imagen.
_a89=ImageTk.PhotoImage((Image.open("Images/a89.png"))) 
a89=Label(t,image=_a89) 
a89.place(x=600,y=600,width=50,height=50) 
from tkinter import messagebox 
from tkinter import filedialog 
cti=ImageTk.PhotoImage((Image.open("Images/changetheimage.png"))) 
ctiw=ImageTk.PhotoImage((Image.open("Images/changetheimagewhite.png"))) 
changetheimage=Label(t,image=cti) 
changetheimage.place(x=0,y=600,width=600,height=50) 
changetheimage.bind("<Enter>",lambda event:changetheimage.config(image=ctiw)) 
changetheimage.bind("<Leave>",lambda event:changetheimage.config(image=cti)) 
def cticlick(event): 
    filetypes = ( 
                ('Images', '*.png'), 
                ('All files', '*.png') 
                )
    t.iconbitmap("Icons/image.ico") 
    e =filedialog.askopenfile(title='Open the image (with the same dimensions)', 
                            initialdir='/', 
                            filetypes=filetypes)
    if e!=None: 
        if Image.open(e.name).width!=Image.open(e.name).height: 
            messagebox.askokcancel("","The image need to has the same dimensions") 
        else: 
            path=e.name 
            listaImagenes.clear() 
            listaImagenesCopia.clear() 
            t.title((" "*60)+"Sliding puzzle | The image is loading ...") 
            cmp=0 
            for i in range(3): 
                for j in range(3): 
                    if i==2 and j==2: 
                        listaImagenes.append(["",cmp]) 
                        listaImagenesCopia.append(["",cmp]) 
                    else: 
                        listaImagenes.append([ImageTk.PhotoImage(Image.open(path).resize((600,600)).crop(((j*200),(i*200),((j*200)+200),((i*200)+200)))),cmp]) 
                        listaImagenesCopia.append([ImageTk.PhotoImage(Image.open(path).resize((600,600)).crop(((j*200),(i*200),((j*200)+200),((i*200)+200)))),cmp]) 
                    cmp+=1
            cos(None)
    t.title((" "*80)+"Sliding puzzle") 
    t.iconbitmap("Icons/w.ico") 
changetheimage.bind("<Button-1>",cticlick) 
from random import shuffle 
b=False 
def f(): 
    global b 
    b=True 
    t.destroy() 
t.protocol("WM_DELETE_WINDOW", f) 
def cos(event): 
    global listaImagenesCopia,Lab,b 
    if event: 
        shuffle(listaImagenesCopia) #Ahora mismo generamos el tablero de manera aleatoria con shuffle, tenemos que implementar
    #el algoritmo de backtracking y generar a partir de dicho algoritmo el tablero.
    for i in range(len(listaImagenesCopia)): 
        Lab[i].config(image=listaImagenesCopia[i][0]) 
        Lab[i].config(bg="#3b53a0") 
    for j in range(len(listaImagenesCopia)): 
        if listaImagenesCopia[j][0]=="": 
            Lab[j].config(bg="#242424") 
    b=True 
    youwin.place_forget() 
    changetheimage.place(x=0,y=600,width=600,height=50) 
restart.bind("<Button-1>",cos) 
#FALTA POR TERMINAR (actualmente general el estado inicial aleatoriamente con shuffle)
def generate_initial_state():
    initial_state = [row[:] for row in FINAL_STATE]  # Copiar el estado final
    empty_row, empty_col = 3, 3  # Posición inicial de la casilla vacía (15)
    for _ in range(300):  # Realizar 1000 movimientos aleatorios
        moves = []
        if empty_row > 0:
            moves.append((-1, 0))  # Mover hacia arriba
        if empty_row < 3:
            moves.append((1, 0))  # Mover hacia abajo
        if empty_col > 0:
            moves.append((0, -1))  # Mover hacia la izquierda
        if empty_col < 3:
            moves.append((0, 1))  # Mover hacia la derecha
        dr, dc = random.choice(moves)  # Seleccionar un movimiento aleatorio
        new_row, new_col = empty_row + dr, empty_col + dc
        initial_state[empty_row][empty_col], initial_state[new_row][new_col] = initial_state[new_row][new_col], initial_state[empty_row][empty_col]  # Intercambiar casillas
        empty_row, empty_col = new_row, new_col  # Actualizar la posición de la casilla vacía
    return initial_state

def state_to_matrix(listaImagenesCopia):
    # Convertir listaImagenesCopia a una matriz de 4x4
    matrix = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            matrix[i][j] = listaImagenesCopia[i * 4 + j][1]
    return matrix

def is_goal(state):
    final_state = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    return state == final_state

def heuristic(state):
    goal_state = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    total_cost = 0
    for i in range(4):
        for j in range(4):
            if state[i][j] != 0:
                row = (state[i][j] - 1) // 4
                col = (state[i][j] - 1) % 4
                total_cost += abs(i - row) + abs(j - col)
    return total_cost


def generate_successors(state):
    successors = []
    # Encontrar la posición de la casilla vacía
    empty_row, empty_col = -1, -1
    for i in range(4):
        for j in range(4):
            if state[i][j] == 15:
                empty_row, empty_col = i, j
                break
    # Mover la casilla vacía hacia arriba, abajo, izquierda y derecha si es posible
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 4 and 0 <= new_col < 4:
            new_state = [row[:] for row in state]  # Copiar el estado actual
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]  # Intercambiar casillas
            successors.append(new_state)
    return successors

def solve_puzzle(initial_state):
    visited = set()
    queue = deque([(initial_state, [])])  # Cola de tuplas: (estado actual, lista de movimientos)
    while queue:
        state, path = queue.popleft()
        if is_goal(state):
            return len(path)
        if tuple(map(tuple, state)) not in visited:
            visited.add(tuple(map(tuple, state)))  # Convertir lista de listas a tupla para hashable
            for successor in generate_successors(state):
                queue.append((successor, path + [successor]))
    return None

def solve_puzzle_a_star(initial_state):
    visited = set()
    pq = PriorityQueue()
    steps_taken = 0
    max_steps = 10000
    pq.put((0, 0, initial_state))  # Tupla: (costo acumulado, pasos restantes, estado actual)
    while not pq.empty() and steps_taken < max_steps:
        cost, steps, state = pq.get()
        if state == [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]:
            return steps
        if tuple(map(tuple, state)) not in visited:
            visited.add(tuple(map(tuple, state)))
            for successor in generate_successors(state):
                h = heuristic(successor)
                g = cost + 1  # Incrementar el costo acumulado
                f = g + h
                pq.put((g, steps + 1, successor))
        steps_taken += 1
    return None

#def get_successors(state):
    # Generar los sucesores del estado actual intercambiando la posición de la pieza vacía con sus vecinos
    successors = []
    empty_row, empty_col = find_empty(state)
    
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 4 and 0 <= new_col < 4:
            new_state = [row[:] for row in state]  # Copiar el estado actual
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
            successors.append(new_state)
    
    return successors

#def find_empty(state):
    # Encuentra la posición de la pieza vacía en el estado actual
    for i in range(4):
        for j in range(4):
            if state[i][j] == 15:
                return i, j

introf=Frame(t) 
introf.place(x=0,y=0,width=650,height=650) 
introi=[ImageTk.PhotoImage(Image.open("Images/1_2.png").resize((300,300))),ImageTk.PhotoImage(Image.open("Images/2_2.png").resize((300,300))),ImageTk.PhotoImage(Image.open("Images/3_2.png").resize((300,300)))] 
introl=Label(introf,bg="#3b53a0") 
introl.place(x=0,y=0,width=650,height=650) 
def intro(): 
    icmp=0 
    ic=0 
     
    while True: 
        introl.config(image=introi[icmp]) 
        sleep(0.2) 
        ic+=1 
        icmp+=1 
        if icmp==3: 
            icmp=0 
        if ic==9: 
            break 
    introf.place_forget() 
    t.geometry(f"650x650") 
    t.overrideredirect(0) 
t.after(1,lambda :Thread(target=intro).start()) 
t.mainloop()