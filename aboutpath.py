import pathlib

def parse_folder(path):
    files = []
    folders = []
    for i in path.iterdir():
        if i.is_file():
            files.append(i.name)
        if i.is_dir():
            folders.append(i.name)
        
            
        
            
    return files, folders

path = pathlib.Path("D:\Projects\Master1")
print(parse_folder(path))
