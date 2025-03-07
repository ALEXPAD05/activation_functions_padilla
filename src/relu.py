import numpy as np  # Importing NumPy for numerical operations
import matplotlib.pyplot as plt  # Importing Matplotlib for plotting

def relu(x):
    # ReLU (Rectified Linear Unit) function
    # Returns the element-wise maximum of 0 and the input x
    return np.maximum(0, x)

def relu_derivative(x):
    # Derivative of the ReLU function
    # Returns 1 where x > 0, and 0 otherwise
    return np.where(x > 0, 1, 0)

def plot_relu():
    # Generate 100 evenly spaced values between -10 and 10 for the x-axis
    x = np.linspace(-10, 10, 100)
    
    # Compute the ReLU function values for the given x values
    y = relu(x)
    
    # Compute the derivative of the ReLU function for the given x values
    y_derivative = relu_derivative(x)

    # Plotting the ReLU function and its derivative
    plt.figure(figsize=(10, 5))  # Create a figure with a specific size
    plt.plot(x, y, label="ReLU", color="blue")  # Plot the ReLU function
    plt.plot(x, y_derivative, label="ReLU Derivative", color="red", linestyle="--")  # Plot the derivative
    plt.title("ReLU Function and its Derivative")  # Set the title of the plot
    plt.xlabel("x")  # Label for the x-axis
    plt.ylabel("y")  # Label for the y-axis
    plt.legend()  # Display the legend
    plt.grid()  # Add a grid to the plot
    plt.show()  # Display the plot