#Question 1

print("Welcome to your SenecaBank savings account. \n")
deposit=float(input("How much would you like to deposit?: $"))
print("\n Deposit successful. Your account has a 4% annual interest rate \n")
print("Your projected savings growth is: \n \n")
print("\t Your Current Balance is: "+str(deposit)+"\n\n")

for i in [1,2,3]:    
    deposit=deposit*1.04
    print("\t After %d year: $%d \n" %(i,deposit))
