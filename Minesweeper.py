from random import randint
from enum import Enum

class GameState(Enum):
    RUNNING = 0
    WIN = 1
    LOSE = -1

class Minesweeper:
    # Wymiary planszy
    BOARD_SIZE = 4

    # Ilość min na planszy
    MINES = 5

    def __init__(self):
        self.board = self.init_board()
        self.revealed_board = [[False]*self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]  # Inicjalizacja ukrytej planszy
        self.state = GameState.RUNNING

    def init_board(self):
        board = [[' ' for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        mines = self.generate_mines(self.MINES)
        for mine in mines:
            board[mine[0]][mine[1]] = '*'
        return board

    def generate_mines(self, num_mines):
        mines = []
        while len(mines) < num_mines:
            mine = randint(0, self.BOARD_SIZE-1), randint(0, self.BOARD_SIZE-1)
            if mine not in mines:
                mines.append(mine)
        return mines

    def print_board(self):
        print("   " + " ".join(str(i) for i in range(self.BOARD_SIZE)))
        print("  " + "-" * (self.BOARD_SIZE*2+1))
        for i, row in enumerate(self.board):
            print(f"{i} |" + " ".join(row))
        print("  " + "-" * (self.BOARD_SIZE*2+1))

    def make_move(self, x, y):
        self.revealed_board[y][x] = True  # Oznaczamy pole jako odkryte
        if self.board[y][x] == '*':
            self.state = GameState.LOSE  # przegrana
            return -10  # Duża ujemna nagroda za przegraną
        else:
            # Znajdź ilość min w sąsiedztwie
            count = 0
            for i in range(max(0, y - 1), min(self.BOARD_SIZE, y + 2)):
                for j in range(max(0, x - 1), min(self.BOARD_SIZE, x + 2)):
                    if self.board[i][j] == '*':
                        count += 1

            self.board[y][x] = str(count)

            # Sprawdź, czy gracz wygrał
            if all(cell != ' ' for row in self.board for cell in row):
                self.state = GameState.WIN  # wygrana
                return 10  # Dodatkowa nagroda za wygraną

            return 1  # Standardowa nagroda za bezpieczny ruch

    def get_state(self):
        state = [[0] * self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                if self.revealed_board[i][j]:  # Jeśli pole jest odkryte
                    if self.board[i][j] == '*':  # Jeśli na polu jest bomba
                        state[i][j] = -1
                    else:  # Jeśli na polu jest liczba (ilość bomb w sąsiedztwie)
                        state[i][j] = int(self.board[i][j])
                else:  # Jeśli pole jest nieodkryte
                    state[i][j] = 0
        return state


