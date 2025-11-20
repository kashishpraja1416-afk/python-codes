# P4: Measurement Conversion

input = int(input("Enter value in inches: "))
foot = input/12
yard = input/36
centimeters = input*2.54
meter = input/39.37

print(f"{input} in foot are {foot}\n")
print(f"{input} in yard are {yard}\n")
print(f"{input} in centimeter are {centimeters}\n")
print(f"{input} in meter are {meter}")