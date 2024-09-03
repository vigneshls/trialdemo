# Define the calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main calculator function
def calculator():
    while True:
        # Display menu options
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        # Take user input for the operation
        choice = input("Enter choice (1/2/3/4/5): ")
        
        # Check if the user wants to exit
        if choice == '5':
            print("Exiting the calculator.")
            break
        
        # Validate the choice
        if choice in ['1', '2', '3', '4']:
            try:
                # Take user input for numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                # Perform the selected operation
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select a valid operation.")

# Run the calculator
if __name__ == "__main__":
    calculator()
    print(Hello World)
