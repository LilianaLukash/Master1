import sys


def parse_args():
    result = ""
    arguments = sys.argv[1:]
    for arg in sys.argv:
        if result=="":
            result = str(arg)
        else:
            result = result + " " + str(arg)
           
            
        
    return result

import sys


def parse_args():
    result = ""
    arguments = sys.argv[1:]
    result = " ".join(arguments)
 
            
        
    return result