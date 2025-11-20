# P7: Avasthi is having some amount of money and he is having only some denominations of 100,50,20,10,5,2,1. 
# He needs to know how many notes are required for the amount present with him. (Do it using Switch case)

amount = int(input("Enter amount: "))
denomination = int(input("Enter denomination: "))
denominations = [100,50,20,10,5,2,1]

match denomination:
    case 100: 
        count100 = amount/100
        var = amount - (count100*100)
        