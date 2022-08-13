import json
import difflib

data=[]
json_file=open('products.json', encoding="utf8")
json_str=json_file.read()
json_data=json.loads(json_str)
json_file.close()

dict_names={}
dict_keys=[]
null_errors=[]


for item in range(len(json_data)):
    try:
        if((json_data[item]["name"].split("-")[0].strip())in dict_names):
            dict_names[(json_data[item]["name"].split("-")[0].strip())].append((json_data[item]["name"])) 
        else:
            dict_names[(json_data[item]["name"].split("-")[0].strip())]=[]
            dict_keys.append((json_data[item]["name"].split("-")[0].strip()))
            dict_names[(json_data[item]["name"].split("-")[0].strip())].append((json_data[item]["name"]))
    except:
        null_errors.append(item)
        continue

if(null_errors):
    print("The following item numbers were removed due to null errors")
    for i in null_errors:
        print(i)

while(True):
    word=input("\n Enter a Word or \'q!\' to exit: ")
    if(word=="q!"):
        print("Exiting!")
        break
    elif(len(word)<=2):
        print("Longer input required")
        continue
    
    word=word.strip().lower().title()
    
    if(word not in dict_keys):
        close_matches=difflib.get_close_matches(word,dict_keys,5,0.5)
        
        if(not close_matches):
            print("There are no matches or close matches to your input \n")
            continue
        else:
            counter=0
            print("Does this match what you are looking for? \n")
            for i in close_matches:
                print("%d %s" %(counter+1,i))
                counter+=1
            
            confirm="n"
            while(confirm=="n"):
                counter=input("Please enter the number which matches the product name you would like to look up: ")
                counter=int(counter)
                confirm=input("Did you mean %s? Enter y if yes, or n for no: " %close_matches[counter-1])
                confirm=confirm.strip().lower()
            

            for i in dict_names[close_matches[counter-1]]:
                print("\n %s" %i)
    else:
        for i in dict_names[word]:
            print(i)


