try:
    a = int(input("Enter a first number: "))
    b = int(input("Enter a second number: "))
    
    print("what kind of operation do you want to perform?.\nPress:\n + for addition\n - for subtraction\n * for multiplication\n / for division")

    o = input("Enter the operation: ")

    match o:
        case "+":
            print(f"The result of {a} + {b} is: {a + b}")
        case "-":
            print(f"The result of {a} - {b} is: {a - b}")
        case "*":
            print(f"The result of {a} * {b} is: {a * b}")
        case "/":
            if b != 0:
                print(f"The result of {a} / {b} is: {a / b}")
            else:
                print("Error: Division by zero is not allowed.")
        case default:
            print("Invalid operation. Please enter +, -, *, or /.")

except Exception as e:

    print("Invalid input. Please enter a valid number.")