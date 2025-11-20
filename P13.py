#P13: Who Wins

stones = int(input("Enter number of stones: "))
i = 1
total = 0
while True:
    total += i
    if total >= stones:
        print("Ramesh won")    
        break

    total += 2*i
    if total >= stones:
        print("Suresh won")
        break 

    i = i + 1    



