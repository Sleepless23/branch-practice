print("This is a newer Python file to test out branching")

num1 = float(input("Enter a Number: "))
num2 = float(input("Enter a Number: "))
pick = int(input("[1 = Add | 2 = Sub | 3 = Mult | 4 = Div] "))

match pick:
    case 1:
        print(num1 + num2)
    case 2:
        print(num1 - num2)
    case 3:
        print(num1 * num2)
    case 4:
        print(num1 / num2)
    case _:
        print("Invalid")