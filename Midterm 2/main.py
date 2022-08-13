import sys
import counter
import most_common as mc
import report as rp

def main():
    file_input=open(sys.argv[1],"r")
    dict_occurences,num_words=counter.count_words(file_input.readlines())
    file_input.close()

    file_output=rp.create_report()

    file_output.write("Report on Input File Analyzed")
    file_output.write("\n")
    file_output.write("---------------------------\n")
    file_output.write("\n")
    file_output.write("The total number of words in the file is :%d" %(num_words))
    file_output.write("\n")
    file_output.write("The number of times each word occured was:")
    file_output.write("\n")

    for a in dict_occurences:
        file_output.write(a+"---> %d  " %dict_occurences[a])
    
    file_output.write("\n")

    frequency_most, words_most=mc.most_common(dict_occurences)
    file_output.write("The most common word occured %d times and is listed below: " %frequency_most)
    file_output.write("\n\n")
    for i in words_most:
        file_output.write(i)
        file_output.write("\n")
    file_output.write("\n")

    frequency_least, number_least=mc.least_common(dict_occurences)
    file_output.write("The least common word occured %d time(s) and is listed below: " %frequency_least)
    file_output.write("\n")
    for i in number_least:
        file_output.write(i)
        file_output.write("\n")
    file_output.write("\n\n")
    
    file_output.close()      


if __name__=="__main__":
    main()