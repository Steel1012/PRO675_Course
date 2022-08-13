# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 13:51:39 2022

@author: shtee
"""

#Midterm Question 1

               
lst= [-2,0,2,3,4,7,9]
lst_matches=[]

low=0
high=len(lst)-1
mid=int((low+high)/2) 


while(low<=high):
    
    if(lst[mid]==mid and mid not in lst_matches):
        lst_matches.append(mid)
        mid+=1 #Once we have a match it is very likely that the following indices will also match.
        continue
    if(lst[mid]<mid): #Using Hint 1
        low=mid+1
    else:
        high=mid-1
    
    mid=(low+high)//2 


lst_matches.sort()
for x in lst_matches:
    print("List index[%d] is equal to the list item %d \n" %(x,x))


