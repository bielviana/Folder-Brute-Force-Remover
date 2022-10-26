import os
from os import path as p
from threading import Thread
import time



os.system('cls')
os.system("title Folder Brute Force Remover")
print('Coded by: Gabriel Viana')
print('https://github.com/pySiriusDev?tab=repositories')
time.sleep(3)



q_list_thread = 200
q_remove_thread = 200
list_tasks = 0
files_tasks = 0
folders_tasks = 0

files = []
files_splitted = []

folders = []
folders_splitted = []



def listDir(init_dir):
    global q_list_thread, files, folders

    q_filenames = 0
    q_subfolders = 0

    print('>> Listing files and subfolders...')
    for dir, subfolders, filenames in os.walk(init_dir):
        q_filenames += len(filenames)
        q_subfolders += len(subfolders)
        for filename in filenames:
            print(p.join(dir, filename))

        print('>> Saving files...')
        for i in range(q_list_thread):
            start = int(i * q_filenames / q_list_thread)
            end = int((i+1) * q_filenames / q_list_thread)
            Thread(target=saveFiles, args=(dir, filenames, start, end)).start()

        print('>> Saving folders...')
        for i in range(q_list_thread):
            start = int(i * q_subfolders / q_list_thread)
            end = int((i+1) * q_subfolders / q_list_thread)
            Thread(target=saveFolders, args=(dir, subfolders, start, end)).start()



def saveFiles(dir, filenames, start, end):
    global list_tasks, files

    for filename in filenames[start:end]:
        filepath = p.join(dir, filename)
        files.append(filepath)
        print(f'>> Added to file list: {filepath}')
    list_tasks += 1



def saveFolders(dir, subfolders, start, end):
    global list_tasks, folders

    for subfolder in subfolders[start:end]:
        folderpath = p.join(dir, subfolder)
        folders.append(folderpath)
        print(f'>> Added to folder list: {folderpath}')
    list_tasks += 1



def deleteFiles(start, end):
    global files, files_tasks

    for file in files[start:end]:
        try:
            print(f'>> File deleted → {file}')
            os.system(f'del /F /S /Q "{file}"')
        except:
            print('>> Error')
    files_tasks += 1



def deleteFolders(start, end):
    global folders, folders_tasks

    for folder in folders[start:end]:
        try:
            print(f'>> Folder deleted → {folder}')
            os.system(f'rd /S /Q "{folder}"')
        except:
            print('>> Error')
    folders_tasks += 1



def checkTasks(init_dir):
    global list_tasks, q_list_thread, q_remove_thread, files, folders, files_tasks, folders_tasks

    while list_tasks < q_list_thread:
        pass

    time.sleep(1)
    os.system('cls')
    print('>> Files listed successfully!\n>> Starting file removal...')
    time.sleep(1)
    os.system('cls')

    q_files = len(files)
    for i in range(q_remove_thread):
        start = int(i * q_files / q_remove_thread)
        end = int((i+1) * q_files / q_remove_thread)
        Thread(target=deleteFiles, args=(start, end)).start()

    while files_tasks < q_remove_thread:
        pass

    time.sleep(1)
    os.system('cls')
    print('>> Files deleted successfully!\n>> Starting folder removal...')
    time.sleep(1)
    os.system('cls')

    q_folders = len(folders)
    for i in range(q_remove_thread):
        start = int(i * q_folders / q_remove_thread)
        end = int((i+1) * q_folders / q_remove_thread)
        Thread(target=deleteFolders, args=(start, end)).start()
    
    while folders_tasks < q_remove_thread:
        pass

    os.system(f'rd /S /Q "{init_dir}"')

    os.system('cls')
    time.sleep(1)
    print('>> Task finalized!')
    exit()



def main():
    init_dir = input('Input the folder you want to remove: ')
    listDir(init_dir)
    Thread(target=checkTasks, args=(init_dir,)).start()



if __name__ == '__main__':
    main()
