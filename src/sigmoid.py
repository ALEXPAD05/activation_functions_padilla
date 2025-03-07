import numpy as np  # Importing NumPy for numerical operations
import matplotlib.pyplot as plt  # Importing Matplotlib for plotting

def sigmoid(x):
    # Sigmoid function
    # Computes the sigmoid of x, which maps any real number to a value between 0 and 1
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    # Derivative of the sigmoid function
    # Computes the derivative of the sigmoid function using the formula: sigmoid(x) * (1 - sigmoid(x))
    sig = sigmoid(x)  # Compute the sigmoid of x
    return sig * (1 - sig)  # Return the derivative

def plot_sigmoid():
    # Generate 100 evenly spaced values between -10 and 10 for the x-axis
    x = np.linspace(-10, 10, 100)
    
    # Compute the sigmoid function values for the given x values
    y = sigmoid(x)
    
    # Compute the derivative of the sigmoid function for the given x values
    y_derivative = sigmoid_derivative(x)

    # Plotting the sigmoid function and its derivative
    plt.figure(figsize=(10, 5))  # Create a figure with a specific size
    plt.plot(x, y, label="Sigmoid", color="blue")  # Plot the sigmoid function
    plt.plot(x, y_derivative, label="Sigmoid Derivative", color="red", linestyle="--")  # Plot the derivative
    plt.title("Sigmoid Function and its Derivative")  # Set the title of the plot
    plt.xlabel("x")  # Label for the x-axis
    plt.ylabel("y")  # Label for the y-axis
    plt.legend()  # Display the legend
    plt.grid()  # Add a grid to the plot
    plt.show()  # Display the plot