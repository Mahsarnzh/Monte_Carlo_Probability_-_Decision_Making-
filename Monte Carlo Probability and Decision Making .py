

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define maze parameters
maze_size = 10
maze = np.zeros((maze_size, maze_size))

# Set the starting position of the circle
start_position = (0, 0)
current_position = start_position

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(0, maze_size)
ax.set_ylim(0, maze_size)

# Plot the maze
ax.imshow(maze, cmap='binary')

# Plot the circle
circle = plt.Circle(start_position, 0.5, color='red')
ax.add_patch(circle)

# Function to update the animation
def update(frame):
    global current_position

    # Generate random steps for the circle's movement
    step = np.random.choice(['up', 'down', 'left', 'right'])
    
    # Update the current position based on the random step
    if step == 'up' and current_position[0] > 0:
        current_position = (current_position[0] - 1, current_position[1])
    elif step == 'down' and current_position[0] < maze_size - 1:
        current_position = (current_position[0] + 1, current_position[1])
    elif step == 'left' and current_position[1] > 0:
        current_position = (current_position[0], current_position[1] - 1)
    elif step == 'right' and current_position[1] < maze_size - 1:
        current_position = (current_position[0], current_position[1] + 1)

    # Update the circle's position in the plot
    circle.set_center(current_position)

# Create the animation
animation = FuncAnimation(fig, update, frames=100, interval=200, repeat=False)

plt.show()
