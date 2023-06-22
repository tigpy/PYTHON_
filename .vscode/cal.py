while True:
    print("Enter 'x' to exit.")
    num1 = input("Enter first number: ")
    if num1 == 'x':
        break
    num2 = input("Enter second number: ")
    if num2 == 'x':
        break
    operator = input("Enter operator (+, -, *, /): ")
    if operator == 'x':
        break

    if operator == '+':
        print(float(num1) + float(num2))
    elif operator == '-':
        print(float(num1) - float(num2))
    elif operator == '*':
        print(float(num1) * float(num2))
    elif operator == '/':
        if num2 == '0':
            print("Error: Cannot divide by zero.")
        else:
            print(float(num1) / float(num2))
    else:
        print("Invalid operator. Please try again.")
