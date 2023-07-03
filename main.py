from Minesweeper import Minesweeper, GameState
from keras.models import load_model
from DQNAgent import DQNAgent
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MinesweeperDQNAgent(DQNAgent):
    def __init__(self, state_size, action_size):
        super().__init__(state_size, action_size)
        self.state = np.zeros((1, state_size))

    def update_state(self, new_state):
        self.state = np.reshape(new_state, (1, self.state_size))

    def choose_action(self):
        return super().act(self.state)

    def train(self, state, action, reward, next_state, done):
        super().train(state, action, reward, np.reshape(next_state, (1, self.state_size)), done)
        self.update_state(next_state)


if __name__ == '__main__':

    NUM_GAMES = 10000  # Define the number of games you want to run
    games = []
    wins = []
    model_scores = []

    for i in range(NUM_GAMES):
        game = Minesweeper()
        state_size = game.BOARD_SIZE * game.BOARD_SIZE
        action_size = game.BOARD_SIZE * game.BOARD_SIZE
        agent = MinesweeperDQNAgent(state_size, action_size)

        model_filename = 'dqn_model.h5'

        try:
            agent.model = load_model(model_filename)
            print("Model loaded.")
        except OSError:
            print("No saved model found. Starting from scratch.")

        moves_counter = 0
        num_wins = 0  # You need to decide how to update this value

        while game.state == GameState.RUNNING:
            action = agent.choose_action()
            x, y = action // game.BOARD_SIZE, action % game.BOARD_SIZE
            reward = game.make_move(x, y)
            moves_counter += 1

            new_state = game.get_state()
            new_state = np.array(new_state).flatten()
            agent.train(agent.state, action, reward, new_state, game.state != GameState.RUNNING)

        if game.state == GameState.WIN:
            print("Win!")
            num_wins += 1  # Update the number of wins
        elif game.state == GameState.LOSE:
            print("Lose!")

        print(f"Number of moves made by the agent: {moves_counter}")

        agent.model.save(model_filename)
        print("Model saved.")

        game = Minesweeper()
        state = game.get_state()
        state = np.array(state).flatten()
        agent.update_state(state)
        moves_counter = 0  # Reset the moves counter

        model_score = 0  # You need to decide how to calculate this value

        games.append(i)
        wins.append(num_wins)
        model_scores.append(model_score)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(games, model_scores, wins, c='r', marker='o')

    ax.set_xlabel('Number of Games')
    ax.set_ylabel('Model Score')
    ax.set_zlabel('Number of Wins')

    plt.show()
    plt.savefig('plot.png')
