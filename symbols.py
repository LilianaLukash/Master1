def real_len(text):
    
    simb =  ["\n", "\f", "\r", "\t", "\v"]
    length = len(text)
    result = length
    for letter in text:
        if letter in simb:
            result-=1
    return result



print(real_len('Alex\nKdfe23\t\f\v.\r'))
