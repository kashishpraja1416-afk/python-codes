# P8: Kevin was doing math operations a lot and he should deliver his task tomorrow. His math’s teacher gives him two numbers a and b. The problem consists of finding the last digit of the potency of the base a and index b. Help Kevin with his problem. You are given two integer numbers: 
# the base a (0 <= a <= 20) and the index b (0 <= b <= 10^10), a and b both are not 0. You have to find the last digit of a^b.
def last_digit(a, b):

    if a == 0:
        return 0
    
    cycle = [a % 10]
    
    for _ in range(3):
        cycle.append((cycle[-1] * (a % 10)) % 10)
    
    return cycle[(b - 1) % 4]

a = int(input("Enter base a: "))
b = int(input("Enter exponent b: "))

