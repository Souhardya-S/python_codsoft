def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")


    choice = input("Enter your choice (1/2/3/4): ")

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please select a valid operation.")
        return


    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Perform the selected operation
    if choice == "1":
        result = num1 + num2
        print(f"The result of addition: {num1} + {num2} = {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"The result of subtraction: {num1} - {num2} = {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"The result of multiplication: {num1} * {num2} = {result}")
    elif choice == "4":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of division: {num1} / {num2} = {result}")


# Run the calculator
calculator()
