from random import randrange

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import numpy as np

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.epsilon = 1.0  # eksploracja na początku
        self.epsilon_min = 0.01  # minimalna wartość epsilon
        self.epsilon_decay = 0.995  # szybkość zmniejszania epsilon
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=Adam())
        return model

    def act(self, state):
        # Losowe działanie z prawdopodobieństwem epsilon
        if np.random.rand() <= self.epsilon:
            return randrange(self.action_size)

        act_values = self.model.predict(state)
        return np.argmax(act_values[0])  # działanie z maksymalną wartością Q

    def train(self, state, action, reward, next_state, done):
        target = self.model.predict(state)
        if done:
            target[0][action] = reward
        else:
            Q_future = max(self.model.predict(next_state)[0])
            target[0][action] = reward + Q_future * 0.95
        self.model.fit(state, target, epochs=1, verbose=0)
        # Zmniejsz epsilon po każdym trenowaniu
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

