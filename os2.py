import os 

FOLDER_NAME = input("Enter the name of directory: ")

if os.path.exists(FOLDER_NAME) :
    print("This folder's name already exists.")

FILE_NAME = input("Enter the file's name: ")
FILE_PATH = os.path.join(FOLDER_NAME, FILE_NAME)

if os.path.exists(FILE_NAME):
    print("This file's name already exists.")
else:
    os.mkdir(FOLDER_NAME)
    CONTENT = input("Enter the content of the file: ")
    with open(FILE_PATH , "w") as file :
        file.write(CONTENT)

    print("File is created.")

