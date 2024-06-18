def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def sqrt(x):
    return x ** 0.5

def power(x, y):
    return x ** y

def main():
    while True:
        print("Select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Exponentiation")
        print("7. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 7:
            break

        num1 = float(input("Enter the first number: "))
        if choice == 5:
            result = sqrt(num1)
        else:
            num2 = float(input("Enter the second number: "))
            if choice == 1:
                result = add(num1, num2)
            elif choice == 2:
                result = subtract(num1, num2)
            elif choice == 3:
                result = multiply(num1, num2)
            elif choice == 4:
                result = divide(num1, num2)
            elif choice == 6:
                result = power(num1, num2)

        print(f"Result: {result:.2f}")
        response = input("Do you want to perform another operation? (y/n): ")
Editar



