import os

def list_directories(path):
    all = os.listdir(path)
    directories = []
    files = []

    for item in os.listdir(path):
        dir_path = os.path.join(path, item)
        if os.path.isdir(dir_path):
            directories.append(item)
        else:
            files.append(item)
    print("Directories:", directories)
    print("Files:", files)
    print("All Directories and Files:", all)


path = r'D:\pp2'

list_directories(path)