import os

source_path = r'D:\pp2\lab6\dir-and-files\song.txt'
destination_path = r'D:\pp2\lab6\dir-and-files\destination_file.txt'

with open(source_path, 'r') as source_file:
    content = source_file.read()

with open(destination_path, 'w') as destination_file:
    destination_file.write(content)


print("Content has been copied")