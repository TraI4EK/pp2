import os

def check_path(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print("The path exists.")
        print("Filename:", filename)
        print("Directory:", directory)
    else:
        print("The path does not exist.")

path = 'D:\osu!\Skins\-         《CK》 Bacon boi 1.0 『blue』'
check_path(path)