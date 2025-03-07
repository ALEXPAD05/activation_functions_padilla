# Importing necessary functions from custom modules
from src.sigmoid import sigmoid, sigmoid_derivative, plot_sigmoid  # Sigmoid function and its derivative, along with plotting function
from src.tanh import tanh, tanh_derivative, plot_tanh            # Tanh function and its derivative, along with plotting function
from src.relu import relu, relu_derivative, plot_relu             # ReLU function and its derivative, along with plotting function

def main():
    # Infinite loop to keep the program running until the user chooses to exit
    while True:
        # Displaying the menu options to the user
        print("Select the function you want to plot:")
        print("1. Sigmoid")
        print("2. ReLU")
        print("3. Tanh")
        print("4. Exit")
        choice = input("Enter the number of your choice: ")  # Taking user input for their choice

        # Handling user input
        if choice == "1":
            plot_sigmoid()  # Plot the sigmoid function
        elif choice == "2":
            plot_relu()     # Plot the ReLU function
        elif choice == "3":
            plot_tanh()     # Plot the tanh function
        elif choice == "4":
            print("Exiting the program...")  # Exit message
            break  # Break the loop to exit the program
        else:
            print("Invalid option. Please try again.")  # Handle invalid input

# Ensuring the script runs only when executed directly, not when imported
if __name__ == "__main__":
    main()