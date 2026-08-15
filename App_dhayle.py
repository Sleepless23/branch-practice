num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
operation = input("What operation would you want to use(+, -, *, /, %)")

if operation == "+":
    print("result:", num1 + num2)
elif operation == "-":
    print("result:", num1 - num2)
elif operation == "*":
    print("result:", num1 * num2)
elif operation == "/":
    print("result:", num1 / num2)
elif operation == "%":
    print("result:", num1 % num2)
else:
    print("invalid operation")