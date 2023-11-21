
# 4 .. 9/14
def is_valid_pin_codes(pin_codes):
    if pin_codes == []:
        return False
    pinset = set(pin_codes)
    if len(pinset) == len(pin_codes):
        for p in pin_codes:
            if type(p) == str and len(p) == 4 :
                try:
                    m = int(p)
                    
                except:
                    return False
            else:
                return False  
        return True        
    else:
        return False
    
print(is_valid_pin_codes(['1101', '9034', '00112']))
print(is_valid_pin_codes(['1101', '9034', '00112']))
