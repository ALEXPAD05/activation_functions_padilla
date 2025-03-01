import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Agregar la carpeta 'src' al path de búsqueda de módulos
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.sigmoid import sigmoid, sigmoid_derivative
from src.tanh import tanh, tanh_derivative
from src.relu import relu, relu_derivative

x = np.linspace(-10, 10, 100)

plt.figure(figsize=(10, 6))

plt.subplot(3, 2, 1)
plt.plot(x, sigmoid(x), label='Sigmoid', color='blue')
plt.title("Sigmoid")
plt.grid()

plt.subplot(3, 2, 2)
plt.plot(x, sigmoid_derivative(x), label='Sigmoid Derivative', color='blue', linestyle='dashed')
plt.title("Sigmoid Derivative")
plt.grid()

plt.subplot(3, 2, 3)
plt.plot(x, tanh(x), label='Tanh', color='red')
plt.title("Tanh")
plt.grid()

plt.subplot(3, 2, 4)
plt.plot(x, tanh_derivative(x), label='Tanh Derivative', color='red', linestyle='dashed')
plt.title("Tanh Derivative")
plt.grid()

plt.subplot(3, 2, 5)
plt.plot(x, relu(x), label='ReLU', color='green')
plt.title("ReLU")
plt.grid()

plt.subplot(3, 2, 6)
plt.plot(x, relu_derivative(x), label='ReLU Derivative', color='green', linestyle='dashed')
plt.title("ReLU Derivative")
plt.grid()

plt.tight_layout()
plt.show()