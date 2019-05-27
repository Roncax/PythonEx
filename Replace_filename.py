import os

# Replace a string in the name of a given tree folder with a string you want
#TODO: only the file should update their name, with the directory it raise a problem with the path
if __name__ == "__main__":
    print('Enter the Path of the files you want to change: ')
    myPath = input()
    print('Now the character you want to change: ')
    oldChar = input()
    print('for the character: ')
    nextChar = input()
    for dirName, subdirList, fileList in os.walk(myPath):
        paths = (os.path.join(root, filename)
            for root, _, filenames in os.walk(myPath)
            for filename in filenames)
        for path in paths:
            newname = path.replace(oldChar, nextChar)
            if newname != path:
                os.rename(path, newname)
