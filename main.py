from ast import walk
from os import path as p
import os
os.system('cls')

folders = []

def main():
    global folders
    for dir, subfolders, filenames in os.walk(p.curdir):
        for file in filenames:
            if '.py' not in file:
                print(p.join(dir, file))
            
        for folder in subfolders:
            folders.append(p.join(dir, folder))

    for f in folders[::-1]:
        try:
            print(f'>> Deleted → {f}')
            os.system(f'rd /S /Q "{f}"')
        except:
            print('>> Error')

main()