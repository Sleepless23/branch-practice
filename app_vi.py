print("Simpol Calc")
num1 = float(input("Enter 1st num:"))
op = input("Enter Operator (+, -, *, /):")
num2 = float(input("Enter 2nd num:"))

if op == '+':
    print(f"Result: {num1 + num2}")
elif op == '-':
    print(f"Result: {num1 - num2}")
elif op == '*':
    print(f"Result: {num1 * num2}")
elif op == '/':
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Can't divided nateenngg")
else:
    print("Invalidddd")