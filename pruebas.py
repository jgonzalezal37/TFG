import random
from queue import Queue
from queue import PriorityQueue
moves = [1,2,3]

matriz = [[11, 10, 4, 7], [2, 9, 8, 0], [14, 1, 6, 3], [12, 5, 15, 13]]
matrix = [[0, 1, 2, 3],[4, 5, 6, 7],[8, 9, 10, 11],[12, 13, 15, 14]]


def generate_successors(state):
    successors = []
    # Encontrar la posición de la casilla vacía
    empty_row, empty_col = -1, -1
    for i in range(4):
        for j in range(4):
            if state[i][j] == 15:  # Modificar este valor si la casilla vacía tiene otro identificador
                empty_row, empty_col = i, j
                break
    # Definir las direcciones de los movimientos
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    # Mover la casilla vacía en todas las direcciones posibles
    for dr, dc in directions:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 4 and 0 <= new_col < 4:
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
        if state == [[0, 1, 2, 3],[4, 5, 6, 7],[8, 9, 10, 11],[12, 13, 14, 15]]:
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


def heuristic(state):
    goal_state = [[0, 1, 2, 3],[4, 5, 6, 7],[8, 9, 10, 11],[12, 13, 14, 15]]
    total_cost = 0
    for i in range(4):
        for j in range(4):
            if state[i][j] != 0:
                row = (state[i][j] - 1) // 4 # (fila 0, 1 o 2) Calcular fila objetivo
                col = (state[i][j] - 1) % 4 # (resto 0, 1 o 2) Calcular columna objetivo
                total_cost += abs(i - row) + abs(j - col) # Sumamos la distancia desde (i,j) hasta (row,col)
    return total_cost


def solve_puzzle_a_star(initial_state):
    # Conjunto para almacenar los estados visitados
    visited = set()
    # Cola de prioridad para almacenar los estados por explorar
    pq = PriorityQueue()
    # Contador de pasos tomados
    steps_taken = 0
    # Número máximo de pasos permitidos
    max_steps = 10000000000
    
    # Agregar el estado inicial a la cola de prioridad
    pq.put((0, 0, initial_state))  # Tupla: (costo acumulado, pasos restantes, estado actual)
    
    # Bucle principal
    while not pq.empty() and steps_taken < max_steps:
        # Obtener el estado con menor costo de la cola de prioridad
        cost, steps, state = pq.get()
        
        # Comprobar si se ha alcanzado el estado objetivo
        if state == [[0, 1, 2, 3],[4, 5, 6, 7],[8, 9, 10, 11],[12, 13, 14, 15]]:
            return steps  # Devolver el número de pasos tomados
        
        # Comprobar si el estado no ha sido visitado previamente
        if tuple(map(tuple, state)) not in visited:
            # Agregar el estado actual al conjunto de estados visitados
            visited.add(tuple(map(tuple, state)))
            
            # Generar sucesores del estado actual
            for successor in generate_successors(state):
                # Calcular la heurística para el sucesor
                h = heuristic(successor)
                # Calcular el costo acumulado para el sucesor
                g = cost + 1  # Incrementar el costo acumulado
                # Calcular la función de evaluación f(n) = g(n) + h(n)
                f = g + h
                # Agregar el sucesor a la cola de prioridad con su costo acumulado y pasos restantes
                pq.put((f, steps + 1, successor))
                #pq (priority queue ordena sus elementos segun el primer elemento que se le pasa, en este caso f)
        # Incrementar el contador de pasos tomados
        steps_taken += 1
    
    # Si se excede el número máximo de pasos permitidos o la cola de prioridad está vacía, retornar None
    return None


def solve_puzzle_dls(initial_state, max_depth=2):
    """
    Resuelve el puzzle Slice 4x4 utilizando búsqueda en profundidad limitada (DLS).
    """
    visited = set()
    stack = [(0, initial_state)]  # (profundidad, estado)
    while stack:
        depth, state = stack.pop()
        if state == [[0, 1, 2, 3],
                     [4, 5, 6, 7],
                     [8, 9, 10, 11],
                     [12, 13, 14, 15]]:
            return depth
        if depth >= max_depth:
            continue
        visited.add(tuple(map(tuple, state)))
        successors = generate_successors(state)
        for successor in successors:
            if tuple(map(tuple, successor)) not in visited:
                stack.append((depth + 1, successor))
    return None 



def verificar_solucionabilidad(estado):
    # Convertir el estado en una lista unidimensional
    estado_unidimensional = [numero for fila in estado for numero in fila if numero != 0]

    # Contar las inversiones
    inversiones = 0
    for i in range(len(estado_unidimensional)):
        for j in range(i + 1, len(estado_unidimensional)):
            if estado_unidimensional[i] > estado_unidimensional[j]:
                inversiones += 1

    # Buscar la fila de la casilla vacía
    fila_casilla_vacia = None
    for fila_index, fila in enumerate(estado):
        if 0 in fila:
            fila_casilla_vacia = fila_index
            break

    # Si la fila de la casilla vacía es impar, agregar 1 a las inversiones
    if fila_casilla_vacia is not None and fila_casilla_vacia % 2 == 0:
        inversiones += 1

    # Verificar si el número total de inversiones es par
    return inversiones % 2 == 0
from random import shuffle
shuffleMatrix = [[7, 15, 5, 9], [10, 8, 3, 11], [13, 0, 14, 4], [1, 12, 2, 6]]
print("Tiene solucion: : ")
print(verificar_solucionabilidad(shuffleMatrix))