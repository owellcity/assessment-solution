import sys
import json
import random

# Excercise Notes:
# Instructions are a bit unclear for me, so I'll answer the way I understood it 

# contains the functions for arithmetic
def add(numbers):
    for i in range(0 , len(numbers) - 1):
        print("{} + {} = {}".format(numbers[i], numbers[i + 1], numbers[i] + numbers[i + 1] ))

def subtract(numbers):
    for i in range(0 , len(numbers) - 1):
        print("{} - {} = {}".format(numbers[i], numbers[i + 1], numbers[i] - numbers[i + 1] ))

def multiply(numbers):
    for i in range(0 , len(numbers) - 1):
        print("{} * {} = {}".format(numbers[i], numbers[i + 1], numbers[i] * numbers[i + 1] ))

def divide(numbers):
    for i in range(0 , len(numbers) - 1):
        print("{} / {} = {}".format(numbers[i], numbers[i + 1], numbers[i] / numbers[i + 1] ))

argNumbers = [] # variable to contain script arguments

if len(sys.argv) == 7: # condition to accept 6 arguments only
    for n in range(1, len(sys.argv)): # loop into the arguments
        if sys.argv[n].isnumeric(): # check if each number is numeric
            argNumbers.append(int(sys.argv[n])) # cast inputs into int

        else: # will terminate the script if there are atleast 1 incorrect input
            print("one of the inputs is not a number!")
            sys.exit(1)

    print("Select which matematical operation to perform:")
    arithmeticOperationChecker = True
    selectedArithmeticOperation = ""

    # will perform the arithmetic based on user input
    while arithmeticOperationChecker:
        arithmeticOperation = input("+ - * /:\n")
        if arithmeticOperation == "+":
            print("Performing Addition..")
            add(argNumbers)
            arithmeticOperationChecker = False
        elif arithmeticOperation == "-":
            print("Performing Subtraction..")
            subtract(argNumbers)
            arithmeticOperationChecker = False
        elif arithmeticOperation == "*":
            print("Performing Multiplication..")
            multiply(argNumbers)
            arithmeticOperationChecker = False
        elif arithmeticOperation == "/":
            print("Performing Division..")
            divide(argNumbers)
            arithmeticOperationChecker = False
        else:
            print("Please select again with correct inputs.. ")

    ### answers / outputs below depending on exercise 2
    print("\n\nPerform subtraction and show output on screen comma separated.")
    subtractionOutputs = []
    for i in range(0 , len(argNumbers) - 1):
        subtractionOutputs.append(str(argNumbers[i] - argNumbers[i + 1]))
    print(",".join(subtractionOutputs))

    print("\n\nPerform multiplication and store result in a JSON file")
    multiplicationOutputs = []

    for i in range(0 , len(argNumbers) - 1):
        multiplicationOutputs.append(str(argNumbers[i] * argNumbers[i + 1]))

    # parsing json data
    jsonData = {}
    for i in range(0 , len(argNumbers)):
        jsonData["InputNumber" + str(i + 1)] = argNumbers[i]
    jsonData["Multiplication"] = ",".join(multiplicationOutputs)

    with open ("multiplication.json", "w+") as file:
        file.write(json.dumps(jsonData))

    print("check if jsonfile is genereted")

    print("\n\nPick randomly a number and show it on screen.")
    print(argNumbers[random.randint(0, len(argNumbers) - 1)])

    print("\n\nPrint sorted (highest to lowest) array/list numbers.")
    print(sorted(argNumbers, reverse=True))

    print("\n\nPrint sorted (lowest to highest) array/list numbers")
    print(sorted(argNumbers))
else: #  will terminate the script if inputs is not exactly 6 arguments
    print("Scipt will accept 6 arguments only")
    print("sample \"python solution_python.py 1 2 3 4 5 6\"")


#try:
#
#except:
#    print("Scipt will accept 6 arguments only")
#    print("python solution_python.py 1 2 3 4 5 6")