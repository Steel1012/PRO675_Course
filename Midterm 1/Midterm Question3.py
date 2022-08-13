
numbers_list=[3,4,1,2,9,8,7,6,5]

dict_matches={

}

for i in numbers_list:
    diff=10-i
    
    if(diff in dict_matches):
        dict_matches[diff]=i
    else:
        dict_matches[i]=1

counter=0
for key,value in dict_matches.items():
    if(value!=1):
        counter+=1
        print("Here is pair %d -> %d:%d \n" %(counter,key,value))
