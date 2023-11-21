def format_ingredients(items):
    
    last = items.pop()
    print(items)
    if not items:
        return last
    first = items[0]
    items = items[1:]
    myli = first

    for i in items:
        myli = myli + ", " + i

    myli =  myli +" and " + last
    
    return myli
a = ['2 eggs']
b = format_ingredients(a)
print(b)