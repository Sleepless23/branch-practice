num1 = int(input("lagay ka number ya:"))
num2 = int(input("isa pa ya"))

operator = (input("enter operator: "))
if operator == "+":
    output = num1 + num2
    print(f"{output}")
elif operator == "-":
    output = num1 - num2
    print(f"{output}")
else:
    print("Invalid")
