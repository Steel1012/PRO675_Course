import string 
import punch_remover as p
import splitter as s
import lower_case as lc

def count_words(file_lines):
    dict_matches={}
    words_counter=0

    for i in file_lines:
        line=lc.lower_case(s.splitter(p.punch_remover(i)))

        for j in line:
            j=j.strip()
            if j=='':
                continue
            else:
                words_counter+=1
                if j in dict_matches:
                    dict_matches[j]+=1
                else:
                    dict_matches[j]=1

    
    return dict_matches, words_counter

