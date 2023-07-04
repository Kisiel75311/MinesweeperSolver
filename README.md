
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>MinesweeperSolver
</h1>
<h3>◦ Solve the puzzle, conquer the mines!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
</p>
<img src="https://img.shields.io/github/languages/top/Kisiel75311/MinesweeperSolver?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/Kisiel75311/MinesweeperSolver?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/Kisiel75311/MinesweeperSolver?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/Kisiel75311/MinesweeperSolver?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project includes code for a Minesweeper game and an agent that can play the game using a Q-table or a Deep Q-Network (DQN) model. The agent learns from its interactions with the game environment and makes decisions based on exploration and exploitation strategies. The code also provides visualization of the game's performance. The project can be used to study and experiment with reinforcement learning algorithms and their application to Minesweeper.

---

## ⚙️ Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**     | The MinesweeperSolver codebase follows a modular architecture that separates the different components of the system. The main.py file serves as the entry point for the Minesweeper game, where an instance of the MinesweeperSolver class is created. It utilizes the DQNAgent class from DQNAgent.py to train and play the game using a Deep Q-Network. The MinesweeperAgent class from MinesweeperAgent.py implements an alternative approach for playing the game using a Q-table. The Minesweeper class from Minesweeper.py is responsible for initializing and managing the game board, generating mines, handling player moves, and game state. Overall, the codebase exhibits a clear separation of concerns, allowing for extensibility and maintainability.    |
| **📖 Documentation**   | The documentation for the MinesweeperSolver codebase is comprehensive and well-structured. Each file in the repository has a brief summary of its functionality and purpose. However, the documentation could benefit from additional explanations of key concepts and design decisions. Code comments are present throughout the codebase, providing clarity on the purpose and functionality of specific sections of code. Overall, the documentation is helpful for understanding the codebase, but could be enhanced to provide more insights and explanations.   |
| **🔗 Dependencies**    | The MinesweeperSolver codebase relies on several external libraries and systems. It uses Keras and TensorFlow for building and training the Deep Q-Network agent. These libraries provide essential functionality for implementing the neural network model and reinforcement learning algorithms. Additionally, the codebase relies on standard Python libraries such as NumPy and random for various utility functions and mathematical operations. These dependencies are well-documented and widely used, ensuring stability and compatibility.   |
| **🧩 Modularity**      | The codebase demonstrates good modularity, with clearly defined and encapsulated components. Each file represents a distinct functionality or module. The MinesweeperSolver class in main.py acts as the main orchestrator, utilizing the DQNAgent and Minesweeper classes to train and play Minesweeper. The DQNAgent class in DQNAgent.py encapsulates the functionality for building and training the Deep Q-Network model. The MinesweeperAgent class in MinesweeperAgent.py provides an alternative implementation using a Q-table. The Minesweeper class in Minesweeper.py handles the game logic and state management. The modular organization of the codebase allows for easy extensibility and maintainability.   |
| **✔️ Testing**          | The codebase does not contain explicit testing strategies or tools. However, the functionality of key components such as the Minesweeper class and the DQNAgent class could benefit from unit tests to ensure their correctness and robustness. Implementing test cases using a testing framework like unittest

---


## 📂 Project Structure




---

## 🧩 Modules

<details closed><summary>Root</summary>

| File                                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [MinesweeperAgent.py](https://github.com/Kisiel75311/MinesweeperSolver/blob/main/MinesweeperAgent.py) | The code snippet defines a MinesweeperAgent class that implements the functionality of an agent that plays the game Minesweeper. The agent uses a Q-table to make decisions on which actions to take. It chooses actions based on a combination of exploration and exploitation strategies. The Q-table is updated based on the agent's experiences and rewards obtained from the game.                                                                                                                                                                          |
| [main.py](https://github.com/Kisiel75311/MinesweeperSolver/blob/main/main.py)                         | The provided code is for a Minesweeper game implemented using a Deep Q-Network (DQN) agent. The agent is trained to play Minesweeper by learning from its interactions with the game environment. It chooses actions based on its current state, updates its state after each action, and receives rewards for each action. The agent's model is saved and loaded to continue training in subsequent games. The code also includes visualization of the game's performance using a 3D scatter plot showing the number of games, model score, and number of wins. |
| [DQNAgent.py](https://github.com/Kisiel75311/MinesweeperSolver/blob/main/DQNAgent.py)                 | The code snippet implements a Deep Q-Network (DQN) agent, using Keras and TensorFlow, for reinforcement learning. The agent has functionalities to build a neural network model, choose actions based on exploration and exploitation, train the model, and update the exploration rate over time.                                                                                                                                                                                                                                                               |
| [Minesweeper.py](https://github.com/Kisiel75311/MinesweeperSolver/blob/main/Minesweeper.py)           | The provided code snippet is for a Minesweeper game. It initializes and manages the game board, generates mines, allows players to make moves, checks for wins and losses, and provides the game state.                                                                                                                                                                                                                                                                                                                                                          |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

### 📦 Installation

1. Clone the MinesweeperSolver repository:
```sh
git clone https://github.com/Kisiel75311/MinesweeperSolver
```

2. Change to the project directory:
```sh
cd MinesweeperSolver
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🎮 Using MinesweeperSolver

```sh
python main.py
```

### 🧪 Running Tests
```sh
pytest
```

---


## 🗺 Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Refactor Y`
> - [ ] `ℹ️ ...`


---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `ℹ️  INSERT-LICENSE-TYPE` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - `ℹ️  List any resources, contributors, inspiration, etc.`

---
