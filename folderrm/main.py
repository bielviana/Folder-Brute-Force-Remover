import os
from os import path as p
from threading import Thread
import time

os.system('cls')



global thread_number, files_tasks, folders_tasks, finished, files, files_splitted, q_files, folders, folders_splitted, q_folders

thread_number = 10
files_tasks = 0
folders_tasks = 0
finished = False

files = []
files_splitted = []
q_files = len(files)

folders = []
folders_splitted = []
q_folders = len(folders)



def listDir():
    for dir, subfolders, filenames in os.walk(p.curdir):
        for filename in filenames:
            if '.py' not in filename:
                files.append(p.join(dir, filename))
            
        for foldername in subfolders:
            folders.append(p.join(dir, foldername))

def deleteFiles(start, end):
    for file in files[start:end]:
        try:
            print(f'>> Deleted → {file}')
            os.system(f'del /F /S /Q "{file}"')
        except:
            print('>> Error')
    files_tasks += 1

def deleteFolders(start, end):
    for folder in folders[start:end:-1]:
        try:
            print(f'>> Deleted → {folder}')
            os.system(f'rd /S /Q "{folder}"')
        except:
            print('>> Error')
    folders_tasks += 1

def checkTasks():
    while files_tasks < 10:
        pass

    time.sleep(1)
    os.system('cls')
    print('>> Files deleted successfully!\n>> Deleting folders...')
    time.sleep(2)
    os.system('cls')

    for i in range(thread_number):
        start = int(i * q_folders / thread_number)
        end = int((i+1) * q_folders / thread_number)
        Thread(target=deleteFolders, args=(start, end)).start()
    
    while folders_tasks < 10:
        pass

    time.sleep(1)
    os.system('cls')
    print('>> Task finalized!')
    os.system('pause')

def main():
    listDir()

    for i in range(thread_number):
        start = int(i * q_files / thread_number)
        end = int((i+1) * q_files / thread_number)
        Thread(target=deleteFiles, args=(start, end)).start()



if __name__ == '__main__':
    main()
    Thread(target=checkTasks).start()