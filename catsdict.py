

def get_cats_info(path):
    with open(path, 'r') as fh:
        slon = []
        allFile= fh.read()
        allList = allFile.split("\n")
        for line in allList:
            line_list = line.split(",")
            slon.append({"id": line_list[0], "name": line_list[1], "age": line_list[2]})
    print(slon)
    return slon

with open("cats.txt", 'w') as fh:
    fh.write('''60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5''')
    
get_cats_info("cats.txt")