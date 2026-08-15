def add(x, y):
    return x + y

def substract(x, y):
    return x - y

print("Simple Addition and Substraction Calculator")
while True:
    choice = input("\nEnter operation (1. +, 2. -, 3. Exit): ")
    if choice == '3':
        break

    if choice in ('1', '2'):
        try:
            num1 = float(input("\nGiven 1: "))
            num2 = float(input("Given 1: "))

            if choice == '1':
                print("Results:", add(num1, num2))

            if choice == '2':
                print("Results:", substract(num1, num2))

        except ValueError:
            print("Invalid input!")
    else:
        print("Invalid choice!")