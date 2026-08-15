# Basilio, Stephen Sedrick C.
# BSIT 3A
# DevNet
# Simple Calculator

no1 = float(input("Number 1: "))
operation = input("Operation (+,-,*,/: ")
no2 = float(input("Number 2: "))

if operation == "+":
    result = no1 + no2
elif operation == "-":
        result = no1 - no2
elif operation == "*":
        result = no1 * no2
elif operation == "/":
    if num2 == 0:
        result = "Cannot be divided by zero."
    else:
        result = no1 / no2
else:
    result = "Operation not available."

print("Result: ", result)