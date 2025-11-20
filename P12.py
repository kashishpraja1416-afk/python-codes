#P12: LCM and GCD
def factors(a):
    b = []
    i = 2
    while i < a:
        if a % i == 0:
            b.append(i)
        i += 1
    return b  

def common(a,b):
    comm = []
    for i in a:
        if i in b:     
            comm.append(i)
    return comm

def GCD(a):
    length = len(a)
    for i in range(length):
        if i == length-1:
            return a[i]

def LCM(a,b):
    greater = max(a,b)
    while True:
        if (greater % a == 0) and (greater % b == 0):
            l = greater
            return l
        greater += 1



n = int(input("Enter numbers: "))
for i in range(n):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    fac1 = factors(num1)
    fac2 = factors(num2)
    comm = common(fac1,fac2)
    ans1 = GCD(comm)
    ans2 = LCM(num1,num2)
    print("GCD is: ",ans1)
    print("Lcm is ",ans2)


