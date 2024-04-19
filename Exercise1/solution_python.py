import os

# get absolute path
absPath = os.getcwd() + "/"

# other path declaration
addedPath = absPath + "deployPackage/added/"
removedPath = absPath + "deployPackage/removed/"

# open and read file content
with open(absPath + "file_diff.txt", "r") as file: 
    fileContent = file.readlines()
    # list comprehension cleanup/strip (\n) new line sequence to the line of content
    fileContent = [line.replace("\n", "") for line in fileContent]

ma = [] # list variable to contain modified or added (M/A)
rd = [] # list variable to contain rename or deleted (R/D)

for line in fileContent:
    # temp variable to contain line content and perform string manipulation
    tmpVar = line.split(" ")

    if tmpVar[0] == "M" or tmpVar[0] == "A":
        ma.append(tmpVar[1].split("/")[-1])

    if tmpVar[0] == "R" or tmpVar[0] == "D":
        rd.append(tmpVar[1].split("/")[-1])

# Create the files
with open(absPath + "added.txt", "w+") as file: 
    [file.write(line + "\n") for line in ma]

with open(absPath + "removed.txt", "w+") as file: 
    [file.write(line + "\n") for line in rd]

# moving the files to the directory
os.rename(absPath + "added.txt", addedPath + "added.txt")
os.rename(absPath + "removed.txt", removedPath + "removed.txt")