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


## Instructions:

# Cloning and Running this Repository on macOS

This guide outlines the steps for macOS users to clone a repository from GitHub and run it on their computer using Bash commands.

## 1. Install Git
If using Homebrew
```
brew install git
```

Ensure that Git is installed on your macOS system. You can install it using Homebrew or download the installer from the official Git website:
https://pages.github.com/


## 2. Clone the Repository
To clone the repository, use the following command:
```
git clone https://github.com/Mahsarnzh/Monte_Carlo_Probability_Decision_Making.git
```

## 3. Navigate to the Repository
Change your working directory to the cloned repository:
```
cd Monte_Carlo_Probability_Decision_Making
```

## 4. Activate Conda Environment
Navigate to the cloned repository directory and activate the Conda environment using the following command:
```
conda activate myenv
```
install required packages for MC_Probability_Decision_Making.py
1. Ensure you have Python installed on your system.
2. Install the required libraries using:
   ```bash
   pip install numpy matplotlib torch
   ```

## 5. Run the Script
Execute the script using the appropriate command based on your python version. For example:

```
python3 Partially_Observable_MC_Probability_Decision_Making.py
```
