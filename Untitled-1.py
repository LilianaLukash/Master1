def capital_text(s):
    s = s.strip()
    
    k = [".","!","?"]
    new_string = s[0].upper
    for n in s:
        if n in k and s.index(n) < len(s):
            new_string = new_string + s[n+1].title
    return new_string