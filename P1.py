# P1: Area of the square wire

angle = int(input("Enter angle: "))
radius = int(input("Radius: "))
pi = 3.14
lengthOfWire = (angle / 360)*2*pi*radius
side = lengthOfWire/4
area = side**2
print("area of square is: " , area)
