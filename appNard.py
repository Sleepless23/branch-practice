print("Basic Own Input")

print("Example this:")

print(" Summary of Final Grade\n Second Semester") # '\n' next line

# print input
avg1 = float(input("Your grade (CC1200P): "))  # first input
avg2 = float(input("Your grade (MCC102): "))
avg3 = float(input("Your grade (MATH101): "))
avg4 = float(input("Your grade (IT21WEBTECH): "))
avg5 = float(input("Your grade (IT21MMS): "))
avg6 = float(input("Your grade (IT12COMORG): "))
avg7 = float(input("Your grade (PE2): "))
avg8 = float(input("Your grade (NSTP2): "))  # last input

total = avg1 + avg2 + avg3 + avg4 + avg5 + avg6 + avg7 + avg8  # collect these number inputs

print(f"{' Subject':<15} {'Grade':>5}")
print(f"{' CC1200P':<15} {avg1:>5.2f}")
print(f"{' MCC102':<15} {avg2:>5.2f}")
print(f"{' MATH101':<15} {avg3:>5.2f}")
print(f"{' IT21WEBTECH':<15} {avg4:>5.2f}")
print(f"{' IT21MMS':<15} {avg5:>5.2f}")
print(f"{' IT12COMORG':<15} {avg6:>5.2f}")
print(f"{' PE2':<15} {avg7:>5.2f}")
print(f"{' NSTP2':<15} {avg8:>5.2f}")

print(f" Total grade: {total:.2f}")

grade = total / 8   # compute the number symbol used

if 50 <= grade <= 100:  # indicate which input between 50 and 100
    
    # conditional statements whichever if added these nested format
    print(f" Average grade: {grade:.2f}")  # converted into another arithmentic symbol

    if 75 <= grade <= 89:  # whatever if number is selection stage
        print(" The result is passed only!")  # message description
    elif 90 <= grade <= 93:
        print(" The result is passed with the top lister is DEAN!")
    elif 94 <= grade <= 97:
        print(" The result is passed with the top lister is PRESIDENT!")
    elif 98 <= grade <= 100:
        print(" The result is passed with the top lister is CHAIRMAN!")
    else:
        print(" The result is failed.")

else:
    print(" Invalid number")  # not too much or too little number input