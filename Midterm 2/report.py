import os

def create_report():

    if(not (os.path.exists("output"))):
        os.mkdir("output")
    os.chdir("output")

    return (open("report.txt","w"))

    

