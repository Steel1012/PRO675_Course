34# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 22:37:53 2022

@author: shtee
"""
#Question 3

print("Welcome to the seconds calculator \n")
user_input=input("Please enter a number of seconds you would like to convert to D:HH:MM:SS format: ")
seconds=int(user_input)
days=0
hours=0
minutes=0
seconds_output=0
output_string=""
second_line=""

while(seconds!=0):
    if((seconds-86400)>=0):#Seconds in a 24 hour period
        days=days+1
        seconds=seconds-86400
        continue
    elif((seconds-3600)>=0):#Seconds in an hour
        hours=hours+1
        seconds=seconds-3600
        continue
    elif((seconds-60)>=0):
        minutes=minutes+1
        seconds=seconds-60
        continue
    else:
        seconds_output=seconds
        seconds=0
        break
    
if(seconds<10):
    output_string=":0"+str(seconds_output)+output_string
else:
    output_string=":"+str(seconds_output)+output_string    

if(minutes<10):
    output_string=":0"+str(minutes)+output_string
else:
    output_string=":"+str(minutes)+output_string    
if(hours<10):
    output_string=":0"+str(hours)+output_string
else:
    output_string=":"+str(hours)+output_string 

output_string=str(days)+output_string
if(days>7):
    second_line="That is Over a week"
elif(minutes>30):
    second_line="That is Over Half an Hour"
else:
    second_line="That is a few minutes"

print(user_input+" Seconds is "+output_string)
print("\n"+second_line)