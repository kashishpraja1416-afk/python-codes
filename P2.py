 #  P2: Maximum of three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

max = "first number" if (a > b and a > c) else "Second number" if b > c else "Third number"
print("Greatest number is : ",max)