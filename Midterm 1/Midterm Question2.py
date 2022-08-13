

while(True):   
    decimal_1=False
    Number_1=input("Please Enter The First Number That You Would Like Compared:")
    if(Number_1.isdigit()):
        print("\nNumber 1= %s\n" %(Number_1))
        break
    elif("."in Number_1 and Number_1.count(".")==1):
        print("\nNumber 1= %s\n" %(Number_1))
        decimal_1=True
        break
    else:
         print("That is Not a Valid Number Please Try Again")
         continue


while(True): 
    decimal_2=False  
    Number_2=input("Please Enter The Second Number That You Would Like Compared:")
    if(Number_2.isdigit()):
        break
    elif("."in Number_2 and Number_2.count(".")==1):
        decimal_2=True
        break
    else:
         print("That is Not a Valid Number Please Try Again")
         continue

original_1=Number_1
original_2=Number_2
counter_1=0
counter_2=0
whole_1=0
whole_2=0
dec_1=0
dec_2=0


if(len(Number_1)>len(Number_2)and not decimal_1 and not decimal_2):
    for i in range(len(Number_1)-len(Number_2)):
        Number_2="0"+Number_2

elif(len(Number_2)>len(Number_1)and not decimal_1 and not decimal_2):
    for i in range(len(Number_2)-len(Number_1)):
        Number_1="0"+Number_1

elif (decimal_1 and decimal_2):
    whole_1=len(Number_1.split(".")[0])
    whole_2=len(Number_2.split(".")[0])

    dec_1=len(Number_1.split(".")[1])
    dec_2=len(Number_2.split(".")[1])

    if(whole_1>whole_2):
        for i in range(whole_1-whole_2):
            Number_2="0"+Number_2
    elif(whole_1<whole_2):
        for i in range(whole_2-whole_1):
            Number_1="0"+Number_1
    if(dec_1>dec_2):
        for i in range(dec_1-dec_2):
            Number_2=Number_2+"0"
    elif(dec_1<dec_2):
        for i in range(dec_2-dec_1):
            Number_1=Number_1+"0"
elif(decimal_1):
    whole_1=len(Number_1.split(".")[0])
    dec_1=len(Number_1.split(".")[1])
    
    if(whole_1>len(Number_2)):
        for i in range(whole_1-len(Number_2)):
            Number_2="0"+Number_2
    elif(len(Number_2)>whole_1):
            for i in range(len(Number_2)-whole_1):
                Number_1="0"+Number_1

    Number_2=Number_2+"."
    for i in range(dec_1):
        Number_2=Number_2+"0"

elif(decimal_2):
    whole_2=len(Number_2.split(".")[0])
    dec_2=len(Number_2.split(".")[1])
    
    if(whole_2>len(Number_1)):
        for i in range(whole_2-len(Number_1)):
            Number_1="0"+Number_1
    elif(len(Number_1)>whole_2):
            for i in range(len(Number_1)-whole_2):
                Number_2="0"+Number_2

    Number_1=Number_1+"."
    for i in range(dec_2):
        Number_1=Number_1+"0"


for i in range(len(Number_1)): 
    if(Number_1[i]>Number_2[i]):
        counter_1+=1
        break
    elif(Number_2[i]>Number_1[i]):
        counter_2+=1
        break
    elif(Number_2[i]==Number_1[i]):
        counter_2+=1
        counter_1+=1


if(counter_1>counter_2):
    print("\n%s is greater than %s" %(original_1,original_2))
elif(counter_1<counter_2):
    print("\n%s is greater than %s" %(original_2,original_1))
elif(counter_1==counter_2):
    print("\n%s is equal to %s" %(original_1,original_2))









