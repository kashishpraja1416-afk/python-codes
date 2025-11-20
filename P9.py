# P9:-Last Digit Of Power.

a, b = map(int, input().split())
last_digit = a % 10
if last_digit in [0, 1, 5, 6]:
    print(last_digit)
else:
    cycle = [pow(last_digit, i, 10) for i in range(1, 5)]
    
    
    index = (b % 4) - 1
    print(cycle[index])
