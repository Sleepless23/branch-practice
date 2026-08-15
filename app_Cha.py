print(Simple add n' Minus Calculator)
num1 = float(input("Enter first number:"))
operator = input("Enter + or -:")
num2 = float(input("Enter second number:"))

if operator == "+":
    result = num1 + num2
print("Answer:", result)

elif operator == "-":
    result = num1 - num2
print("Answer:", result)

else
print("Invalid operator")
