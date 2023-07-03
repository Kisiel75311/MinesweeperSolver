import numpy as np

class MinesweeperAgent:
    def __init__(self, game):
        self.game = game
        self.q_table = np.zeros([self.game.BOARD_SIZE, self.game.BOARD_SIZE, 2])

    def choose_action(self):
        # Wybór akcji: eksploracja vs eksploatacja
        if np.random.uniform(0, 1) < 0.8: # 30% szans na eksplorację
            # Wybieranie losowego ruchu (eksploracja)
            x = np.random.randint(self.game.BOARD_SIZE)
            y = np.random.randint(self.game.BOARD_SIZE)
        else:
            # Wybieranie ruchu z Q-table (eksploatacja)
            state = self.get_state()
            x, y = np.unravel_index(self.q_table[state].argmax(), (self.game.BOARD_SIZE, self.game.BOARD_SIZE))
        return x, y

    def get_state(self):
        # Pobierz aktualny stan planszy
        board = self.game.board

        # Inicjalizuj pustą tablicę stanu o tych samych wymiarach, co plansza
        state = np.empty_like(board, dtype=np.int)

        # Przekształć wartości na planszy na liczby całkowite dla tablicy stanu
        for i in range(self.game.BOARD_SIZE):
            for j in range(self.game.BOARD_SIZE):
                if self.game.revealed_board[i][j]:  # jeżeli pole jest odkryte
                    if board[i][j] == '*':
                        state[i][j] = -1  # oznaczamy minę
                    elif board[i][j] == ' ':
                        state[i][j] = 0  # oznaczamy puste pole
                    else:
                        state[i][j] = int(board[i][j])  # zapisujemy ilość min wokół
                else:
                    state[i][j] = -2  # jeżeli pole jest nieodkryte, oznaczamy to specjalnym symbolem

        return state

    def update_q_table(self, old_state, action, reward, new_state):
        # Zamień krotkę akcji na pojedynczy indeks
        action_index = action[0] * self.game.BOARD_SIZE + action[1]

        # Wyciągnij poprzednią wartość z q_table
        # old_value = self.q_table[tuple(old_state)][action_index]

        # Oblicz nową wartość
        future_max_value = np.max(self.q_table[tuple(new_state)])
        new_value = reward + 0.9 * future_max_value

        # Aktualizuj q_table
        self.q_table[tuple(old_state)][action_index] = new_value


