# Activation Functions Visualization

This project provides a simple Python program to visualize and compare three common activation functions used in machine learning and neural networks: **Sigmoid**, **ReLU**, and **Tanh**. It also includes their derivatives, which are essential for backpropagation in neural networks.

## Activation Functions Included

1. **Sigmoid Function**:
   - Formula: \( \sigma(x) = \frac{1}{1 + e^{-x}} \)
   - Derivative: \( \sigma'(x) = \sigma(x) \cdot (1 - \sigma(x)) \)
   - Output Range: \( (0, 1) \)

2. **ReLU (Rectified Linear Unit) Function**:
   - Formula: \( \text{ReLU}(x) = \max(0, x) \)
   - Derivative: \( \text{ReLU}'(x) = \begin{cases} 1 & \text{if } x > 0 \\ 0 & \text{otherwise} \end{cases} \)
   - Output Range: \( [0, \infty) \)

3. **Tanh (Hyperbolic Tangent) Function**:
   - Formula: \( \text{tanh}(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} \)
   - Derivative: \( \text{tanh}'(x) = 1 - \text{tanh}(x)^2 \)
   - Output Range: \( (-1, 1) \)

## How It Works

The program consists of the following components:

1. **`sigmoid.py`**:
   - Contains the implementation of the Sigmoid function and its derivative.
   - Includes a `plot_sigmoid()` function to visualize the Sigmoid function and its derivative.

2. **`relu.py`**:
   - Contains the implementation of the ReLU function and its derivative.
   - Includes a `plot_relu()` function to visualize the ReLU function and its derivative.

3. **`tanh.py`**:
   - Contains the implementation of the Tanh function and its derivative.
   - Includes a `plot_tanh()` function to visualize the Tanh function and its derivative.

4. **`main.py`**:
   - Provides a menu-driven interface for the user to select which activation function to plot.
   - The user can choose between Sigmoid, ReLU, Tanh, or exit the program.

## How to Run the Program

1. Clone the repository or download the source code.
2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
3. Run the main.py file:
   ```bash
   python main.py
4. Follow the on-screen instructions to select and visualize the activation functions.