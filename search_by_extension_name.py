import os
import shutil
import datetime

found_num = 0
keys = []
is_copyfile = True
copy_path = ''


def dfs(path):
    global found_num
    try:
        files = os.listdir(path)
    except FileNotFoundError:
        return
    for file in files:
        if os.path.isfile(path + '\\' + file):
            for key in keys:
                if key in file:
                    found_num += 1
                    print(found_num, file)
                    if is_copyfile:
                        shutil.copyfile(path + '\\' + file, copy_path + '\\' + file)
                    break
        else:
            try:
                if os.path.isdir(path + '\\' + file):
                    dfs(path + '\\' + file)
            except PermissionError:
                pass


def search_by_extension_name():
    global keys
    global is_copyfile
    global copy_path
    print('Do not add \\ to the end of all paths!')
    path = input('Please input the start path:')
    keys = input('Please input the file\'s extension name(Use , separate):')
    keys = keys.split(',')
    is_copy = input('If you need to copy this found files to a path(y/n):')
    if is_copy == 'y' or is_copy == 'Y':
        is_copyfile = True
        copy_path = input('Please input the copy path:')
        while not os.path.isdir(copy_path):
            print('Wrong path! please input again.')
            copy_path = input('Please input the copy path:')
    starttime = datetime.datetime.now()
    dfs(path)
    endtime = datetime.datetime.now()
    print('>>>Finish! It spent', (endtime - starttime).seconds, 'sec.', found_num, 'files were found.')


if __name__ == '__main__':
    search_by_extension_name()
