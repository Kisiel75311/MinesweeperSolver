from Minesweeper import Minesweeper, GameState
from keras.models import load_model
from DQNAgent import DQNAgent
import numpy as np

class MinesweeperDQNAgent(DQNAgent):
    def __init__(self, state_size, action_size):
        super().__init__(state_size, action_size)
        self.state = np.zeros((1, state_size))

    def update_state(self, new_state):
        self.state = np.reshape(new_state, (1, state_size))

    def choose_action(self):
        return super().act(self.state)

    def train(self, action, reward, new_state, done):
        super().train(self.state, action, reward, np.reshape(new_state, (1, state_size)), done)
        self.update_state(new_state)


if __name__ == '__main__':
    game = Minesweeper()
    state_size = game.BOARD_SIZE * game.BOARD_SIZE
    action_size = game.BOARD_SIZE * game.BOARD_SIZE
    agent = MinesweeperDQNAgent(state_size, action_size)

    model_filename = 'dqn_model.h5'

    # Wczytaj model DQN, jeśli istnieje
    try:
        agent.model = load_model(model_filename)
        print("Wczytano model DQN.")
    except OSError:
        print("Nie znaleziono zapisanego modelu DQN. Rozpoczynanie od zera.")

    moves_counter = 0  # Inicjalizacja licznika ruchów
    counter = 0
    while True:
        counter += 1
        while game.state == GameState.RUNNING:
            game.print_board()
            action = agent.choose_action()
            x, y = action // game.BOARD_SIZE, action % game.BOARD_SIZE
            print(f"Ruch agenta: {x}, {y}")
            reward = game.make_move(x, y)
            moves_counter += 1  # Zwiększanie licznika ruchów po każdym ruchu agenta

            # Zaktualizuj stan agenta i przeprowadź uczenie
            new_state = game.get_state().flatten()
            agent.train(action, reward, new_state, game.state != GameState.RUNNING)

        game.print_board()
        if game.state == GameState.WIN:
            print("Wygrana!")
            break
        elif game.state == GameState.LOSE:
            print("Przegrana!")

        # Wyświetl licznik ruchów
        print(f"Liczba ruchów agenta: {moves_counter}")

        # Zapisz model DQN
        agent.model.save(model_filename)
        print("Zapisano model DQN.")

        # Inicjalizuj nową grę i zresetuj stan agenta
        game = Minesweeper()
        agent.update_state(game.get_state().flatten())
        moves_counter = 0  # Zresetuj licznik ruchów

        print("Counter: ", counter)
