import os
from os import path as p

os.system('cls')

init_dir = input('Folder to delete: ')

def main(): 
    folders = []

    for dir, subfolders, filenames in os.walk(init_dir):
        for file in filenames:
            if '.py' not in file:
                try:
                    os.system(f'del /F /S /Q "{p.join(dir, file)}"')
                    print(f'>> Deleted → {p.join(dir, file)}')
                except:
                    print('>> Error')
            
        for folder in subfolders:
            folders.append(p.join(dir, folder))

    for f in folders[::-1]:
        try:
            print(f'>> Deleted → {f}')
            os.system(f'rd /S /Q "{f}"')
        except:
            print('>> Error')
    
    try:
        os.system(f'rd /S /Q "{init_dir}"')
    except:
        print('>> Error')

main()
