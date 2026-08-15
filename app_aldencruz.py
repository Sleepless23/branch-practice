n1 = int(input("Enter num1: "))

n2 = int(input("Enter num2: "))

operator = (input("Enter operator: "))
if operator == "+":
    output = n1 + n2
    print(f"{output}")
elif operator == "-":
    output = n1 - n2
    print(f"{output}")
else:
    print("Invalid")
