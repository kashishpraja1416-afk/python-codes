# P6: Reverse Number

def reverse(k): 
    rev = 0
    while k > 0:
        digit = k % 10         
        rev = rev * 10 + digit 
        k = k // 10            
    return rev

n = int(input("Enter number: "))

for i in range(n):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    arev = reverse(a)
    brev = reverse(b)
    sum = arev + brev
    sumrev = reverse(sum)
    print(f"final output is {sumrev}")    