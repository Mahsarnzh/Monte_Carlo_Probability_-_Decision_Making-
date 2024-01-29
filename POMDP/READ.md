## Monte Carlo Probability Decision Making

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

### How to Run
1. Ensure you have Python installed on your system.
2. Install the required libraries using:
   ```bash
   pip install numpy matplotlib torch
