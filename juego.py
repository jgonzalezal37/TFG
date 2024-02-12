import tkinter as tk
import random

class PuzzleGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("N Puzzle")
        self.board_frame = tk.Frame(self.master)
        self.board_frame.pack()

        self.generate_board()
        self.shuffle_board()
        

    def generate_board(self):
        numbers = list(range(16))
        random.shuffle(numbers)

        self.cells = []
        self.empty_row = self.empty_col = None
        idx = 0
        for i in range(4):
            row = []
            for j in range(4):
                cell_value = numbers[idx]
                cell = tk.Button(self.board_frame, text=cell_value, width=5, height=2, font=('Helvetica', 16, 'bold'), bg='#ccc', relief=tk.RAISED, command=self.handle_click)
                cell.grid(row=i, column=j, padx=3, pady=3)
                row.append(cell)
                if cell_value == 0:
                    self.empty_row, self.empty_col = i, j
                
                # Agregar evento bind a la etiqueta de la casilla
                cell.bind("<Button-1>", lambda event, row=i, col=j: self.handle_click(event, row, col))
                
                idx += 1
            self.cells.append(row)


        shuffle_button = tk.Button(self.master, text="Shuffle", command=self.shuffle_board)
        shuffle_button.pack(pady=10)

    def handle_click(self, event, row, col):
        print("Celda clickeada:", row, col)
        cell = self.cells[row][col]
        print("Valor de la celda:", cell["text"])  # Imprime el valor de la celda

    def shuffle_board(self):
        numbers = list(range(16))
        random.shuffle(numbers)

        self.cells = []
        self.empty_row = self.empty_col = None
        idx = 0
        for i in range(4):
            row = []
            for j in range(4):
                cell_value = numbers[idx]
                cell = tk.Button(self.board_frame, text=cell_value, width=5, height=2, font=('Helvetica', 16, 'bold'), bg='#ccc', relief=tk.RAISED, command=self.handle_click)
                cell.grid(row=i, column=j, padx=3, pady=3)
                row.append(cell)
                if cell_value == 0:
                    self.empty_row, self.empty_col = i, j
                
                # Agregar evento bind a la etiqueta de la casilla
                cell.bind("<Button-1>", lambda event, row=i, col=j: self.handle_click(event, row, col))
                
                idx += 1
            self.cells.append(row)

    def is_adjacent(self, row, col):
        return abs(row - self.empty_row) + abs(col - self.empty_col) == 1

    def move_cell(self, row, col):
        if self.is_adjacent(row, col):
            self.cells[row][col].grid(row=self.empty_row, column=self.empty_col)
            self.cells[self.empty_row][self.empty_col].grid(row=row, column=col)
            self.cells[row][col], self.cells[self.empty_row][self.empty_col] = self.cells[self.empty_row][self.empty_col], self.cells[row][col]
            self.empty_row, self.empty_col = row, col


def main():
    root = tk.Tk()
    app = PuzzleGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
