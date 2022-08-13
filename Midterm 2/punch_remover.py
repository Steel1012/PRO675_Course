import string

def punch_remover(line):
    return line.translate(str.maketrans('','',string.punctuation))