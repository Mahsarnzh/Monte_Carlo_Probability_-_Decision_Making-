# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.patches import Circle
# from matplotlib.animation import FuncAnimation
# import torch
# import torch.nn as nn
# import torch.optim as optim

# # Define maze parameters
# maze_size = 10
# start_position = (0, 0)
# end_position = (maze_size - 1, maze_size - 1)

# # Initialize maze
# maze = np.zeros((maze_size, maze_size))

# # Initialize agent position
# agent_position = start_position

# # Initialize Matplotlib plot
# fig, ax = plt.subplots()
# ax.set_xlim(0, maze_size)
# ax.set_ylim(0, maze_size)
# circle = Circle(start_position, radius=0.4, color='red')
# ax.add_patch(circle)

# # Define reward and punishment values
# reward_value = 1
# punishment_value = -1

# # Define neural network model
# class DecisionNetwork(nn.Module):
#     def __init__(self, input_size, hidden_size, output_size):
#         super(DecisionNetwork, self).__init__()
#         self.fc1 = nn.Linear(input_size, hidden_size)
#         self.relu = nn.ReLU()
#         self.fc2 = nn.Linear(hidden_size, output_size)

#     def forward(self, x):
#         x = self.fc1(x)
#         x = self.relu(x)
#         x = self.fc2(x)
#         return x

# # Initialize neural network model
# input_size = 2  # Size of input (agent's current position)
# hidden_size = 8
# output_size = 4  # Number of possible moves (up, down, left, right)
# decision_net = DecisionNetwork(input_size, hidden_size, output_size)
# optimizer = optim.Adam(decision_net.parameters(), lr=0.001)

# # Function to update the plot and agent's position
# def update(frame):
#     global agent_position

#     # Convert agent's position to one-hot encoding
#     input_data = np.zeros((1, input_size))
#     input_data[0, 0] = agent_position[0]
#     input_data[0, 1] = agent_position[1]

#     # Convert to PyTorch tensor
#     input_tensor = torch.tensor(input_data, dtype=torch.float32)

#     # Forward pass through the neural network
#     output = decision_net(input_tensor)

#     # Choose the move with the highest output score
#     best_move = torch.argmax(output).item()

#     # Update agent's position
#     if best_move == 0 and agent_position[0] > 0 and agent_position[0] < maze_size - 1:
#         agent_position = (agent_position[0] - 1, agent_position[1])
#     elif best_move == 1 and agent_position[0] < maze_size - 1:
#         agent_position = (agent_position[0] + 1, agent_position[1])
#     elif best_move == 2 and agent_position[1] > 0:
#         agent_position = (agent_position[0], agent_position[1] - 1)
#     elif best_move == 3 and agent_position[1] < maze_size - 1:
#         agent_position = (agent_position[0], agent_position[1] + 1)


#     # Update the circle's position in the plot
#     circle.set_center(agent_position)


# # Create animation
# animation = FuncAnimation(fig, update, frames=range(100), interval=500, repeat=False)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from matplotlib.animation import FuncAnimation
import torch
import torch.nn as nn
import torch.optim as optim

# Define maze parameters
maze_size = 10
start_position = (0, 0)

# Initialize agent position
agent_position = start_position

# Generate a random target position
target_position = (np.random.randint(0, maze_size), np.random.randint(0, maze_size))

# Initialize Matplotlib plot
fig, ax = plt.subplots()
ax.set_xlim(0, maze_size)
ax.set_ylim(0, maze_size)

# Add a square to represent the target position
target_square = Rectangle(target_position, 1, 1, linewidth=1, edgecolor='yellow', facecolor='yellow')
ax.add_patch(target_square)

# Add a circle to represent the agent position
circle = Circle(start_position, radius=0.4, color='red')
ax.add_patch(circle)

# Define reward and punishment values
reward_value = 1
punishment_value = -1


# Define neural network model
class DecisionNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(DecisionNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Initialize neural network model
input_size = 2  # Size of input (agent's current position)
hidden_size = 8
output_size = 4  # Number of possible moves (up, down, left, right)
decision_net = DecisionNetwork(input_size, hidden_size, output_size)
optimizer = optim.Adam(decision_net.parameters(), lr=0.001)

# Function to update the plot and agent's position
def update(frame):
    global agent_position

    # Calculate the direction towards the target position
    direction = (target_position[0] - agent_position[0], target_position[1] - agent_position[1])

    # Convert direction to a move (up, down, left, right)
    if np.abs(direction[0]) > np.abs(direction[1]):
        best_move = 0 if direction[0] < 0 else 1
    else:
        best_move = 2 if direction[1] < 0 else 3

    # Update agent's position
    if best_move == 0 and agent_position[0] > 0:
        agent_position = (agent_position[0] - 1, agent_position[1])
    elif best_move == 1 and agent_position[0] < maze_size - 1:
        agent_position = (agent_position[0] + 1, agent_position[1])
    elif best_move == 2 and agent_position[1] > 0:
        agent_position = (agent_position[0], agent_position[1] - 1)
    elif best_move == 3 and agent_position[1] < maze_size - 1:
        agent_position = (agent_position[0], agent_position[1] + 1)

    # Update the circle's position in the plot
    circle.set_center(agent_position)

# Create animation
animation = FuncAnimation(fig, update, frames=range(100), interval=500, repeat=False)
plt.show()
