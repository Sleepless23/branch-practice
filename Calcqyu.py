#ASGDHHSAGHDASGHDG

# Source - https://stackoverflow.com/a/63854252
# Posted by tiago barsan, modified by community. See post 'Timeline' for change history
# Retrieved 2026-08-15, License - CC BY-SA 4.0



print ("hello world")
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
print("Would you like to add or subtract?")
txt = input("Type 'a' for add or 's' for subtract")
if txt == "a" or txt=="A":
    z = x + y 
elif txt == "s" or txt=="S":
    z = x - y 
print (z)
