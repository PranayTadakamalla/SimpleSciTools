import math

# Function to display the menu of operations
def display_menu():
    print("\nScientific Calculator Menu:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (x^y)")
    print("6. Square Root (√x)")
    print("7. Logarithm (log(x))")
    print("8. Sine (sin(x))")
    print("9. Cosine (cos(x))")
    print("10. Tangent (tan(x))")
    print("11. Exit")
    
# Function to perform arithmetic operations
def calculator():
    while True:
        display_menu()
        choice = input("Enter the operation you want to perform (1-11): ")

        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        
        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        
        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error! Division by zero.")
        
        elif choice == '5':
            base = float(input("Enter base number: "))
            exponent = float(input("Enter exponent: "))
            print(f"Result: {base} ^ {exponent} = {base ** exponent}")
        
        elif choice == '6':
            num = float(input("Enter the number: "))
            if num >= 0:
                print(f"Result: √{num} = {math.sqrt(num)}")
            else:
                print("Error! Square root of a negative number is not defined.")
        
        elif choice == '7':
            num = float(input("Enter the number: "))
            if num > 0:
                print(f"Result: log({num}) = {math.log(num)}")
            else:
                print("Error! Logarithm of a non-positive number is not defined.")
        
        elif choice == '8':
            angle = float(input("Enter angle in degrees: "))
            print(f"Result: sin({angle}) = {math.sin(math.radians(angle))}")
        
        elif choice == '9':
            angle = float(input("Enter angle in degrees: "))
            print(f"Result: cos({angle}) = {math.cos(math.radians(angle))}")
        
        elif choice == '10':
            angle = float(input("Enter angle in degrees: "))
            print(f"Result: tan({angle}) = {math.tan(math.radians(angle))}")
        
        elif choice == '11':
            print("Exiting the calculator. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please choose a valid option.")

# Start the calculator
calculator()
