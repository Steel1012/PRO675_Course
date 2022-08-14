#Question 2

print("Thank You For Shopping at Seneca Mart. \n")
cash=float(input("How much change is required? Please input an amount in cents: "))

toonies=0
loonies=0
quarters=0
dimes=0
nickels=0
pennies=0

while(cash!=0):
    if((cash-200)>=0):
        toonies=toonies+1
        cash=cash-200
        continue
    elif((cash-100)>=0):
        loonies=loonies+1
        cash=cash-100
        continue
    elif((cash-25)>=0):
        quarters=quarters+1
        cash=cash-25
        continue
    elif((cash-10)>=0):
        dimes=dimes+1
        cash=cash-10
        continue
    elif((cash-5)>=0):
        nickels=nickels+1
        cash=cash-5
        continue
    else:
        pennies=int(cash)
        cash=0
        break
    
total=int(toonies+loonies+quarters+dimes+nickels+pennies)

print("The following coins will be dispensed: \n \n")
print("\t Toonies: "+str(toonies)+"\n")
print("\t Loonies: "+str(loonies)+"\n")
print("\t Quarters: "+str(quarters)+"\n")
print("\t Dimes: "+str(dimes)+"\n")
print("\t Nickels: "+str(nickels)+"\n")
print("\t Pennies: "+str(pennies)+"\n")

print("You will receive %d coins in total" %(total))



