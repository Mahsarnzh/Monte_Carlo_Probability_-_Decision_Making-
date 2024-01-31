# Code Overview for Partially_Observable_MonteCarlo_Probability_DecisionMaking_Process

- The maze is represented as a 2D array with zeros indicating empty spaces.
- The circle is represented by a red circle patch in the Matplotlib plot.
- The `update` function generates random steps for the circle's movement and updates its position accordingly.
- The animation is created using `FuncAnimation` from Matplotlib.

# Random Walk in a Maze Animation
This Python script generates an animated random walk of a circle in a maze using Matplotlib. The circle starts at a specified position in the maze and takes random steps (up, down, left, or right) at each frame.

![Sample frame](https://github.com/Mahsarnzh/Monte_Carlo_Probability_Decision_Making/blob/main/Monte_Carlo_Probability_Decision_Making/MDP.png)



# Code Overview for POMDP (Partially Observable Monte Carlo Decision Process

### Overview
This repository contains Python code for simulating a simple agent in a maze environment using Monte Carlo probability-based decision making. The code utilizes Matplotlib for visualization and PyTorch for implementing a neural network model that guides the agent's decisions.

### Key Components
1. **Agent Movement Simulation:**
   - The agent moves in a maze environment based on Monte Carlo probability decision making.
   - The maze is represented as a grid, and the agent aims to reach a randomly generated target position.

2. **Neural Network Model:**
   - A simple neural network model is implemented using PyTorch.
   - The neural network takes the agent's current position as input and outputs probabilities for possible moves (up, down, left, right).

3. **Visualization:**
   - The agent's movements are visualized using Matplotlib.
   - The current position of the agent is represented by a red circle, and the target position is represented by a yellow square.

![Sample frame](https://github.com/Mahsarnzh/Monte_Carlo_Probability_Decision_Making/blob/main/POMDP/POMDP.png)


# for more information on how to run the codes, follow instructions on READ.md in each folder
