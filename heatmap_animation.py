import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a random 10x10 grid of data points
data = np.random.rand(10, 10)

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the heatmap plot
heatmap = ax.imshow(data, cmap='inferno')

# Define the animation function
def animate(frame):
    # Shift the data array to simulate the snake "eating"
    data[:-1] = data[1:]
    data[-1] = np.random.rand(10)  # Randomly generate new data for the last row
    heatmap.set_array(data)  # Update the heatmap data

# Set up the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=200)

plt.colorbar(heatmap)  # Add a colorbar for reference
plt.title('Snake Eating Heatmap Animation')
plt.show()
