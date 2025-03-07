import numpy as np  # Importing NumPy for numerical operations
import matplotlib.pyplot as plt  # Importing Matplotlib for plotting

def tanh(x):
    # Tanh (Hyperbolic Tangent) function
    # Computes the hyperbolic tangent of x, which maps any real number to a value between -1 and 1
    return np.tanh(x)

def tanh_derivative(x):
    # Derivative of the Tanh function
    # Computes the derivative of the Tanh function using the formula: 1 - tanh(x)^2
    return 1 - np.tanh(x)**2

def plot_tanh():
    # Generate 100 evenly spaced values between -10 and 10 for the x-axis
    x = np.linspace(-10, 10, 100)
    
    # Compute the Tanh function values for the given x values
    y = tanh(x)
    
    # Compute the derivative of the Tanh function for the given x values
    y_derivative = tanh_derivative(x)

    # Plotting the Tanh function and its derivative
    plt.figure(figsize=(10, 5))  # Create a figure with a specific size
    plt.plot(x, y, label="Tanh", color="blue")  # Plot the Tanh function
    plt.plot(x, y_derivative, label="Tanh Derivative", color="red", linestyle="--")  # Plot the derivative
    plt.title("Tanh Function and its Derivative")  # Set the title of the plot
    plt.xlabel("x")  # Label for the x-axis
    plt.ylabel("y")  # Label for the y-axis
    plt.legend()  # Display the legend
    plt.grid()  # Add a grid to the plot
    plt.show()  # Display the plot