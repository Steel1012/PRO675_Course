import sys

def most_common(sorted_dict):
    frequency=0
    most_common=[]

    for i in sorted_dict:
        if sorted_dict[i]>frequency:
            frequency=sorted_dict[i]
        
    for j in sorted_dict:
        if sorted_dict[j]==frequency:
            most_common.append(j)
    
    return frequency, most_common

def least_common(sorted_dict):
    frequency=sys.maxsize
    least_common=[]

    for i in sorted_dict:
        if sorted_dict[i]<frequency:
            frequency=sorted_dict[i]
        
    for j in sorted_dict:
        if sorted_dict[j]==frequency:
            least_common.append(j)
    
    return frequency, least_common

    

    
