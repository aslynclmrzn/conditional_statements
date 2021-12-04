# Program 1: Number Sorter
# Ask for 4 numbers
inputA =  float(input('Enter 1st value : '))
inputB =  float(input('Enter 2nd value : '))
inputC =  float(input('Enter 3rd value : '))
inputD = float(input('Enter 4th value : '))

# Conditional statements that print the 4 numbers from highest to lowest.

if ( inputA >= inputB) and (inputA >= inputC) and (inputA >= inputD) :
    if (inputA >= inputB >= inputC >= inputD):
        print("The sorted list is:", inputA, inputB, inputC, inputD)
    elif (inputA >= inputC >= inputB >= inputD):
        print("The sorted list is:", inputA, inputC, inputB,inputD)
    elif (inputA >= inputD >= inputB >= inputC):
        print("The sorted list is:", inputA, inputD, inputB,inputC)
    elif (inputA >= inputB >= inputD >= inputC):
        print("The sorted list is:", inputA, inputB, inputD,inputC)
    elif (inputA >= inputC >= inputD >= inputB):
        print("The sorted list is:", inputA, inputC, inputD,inputB)
    elif (inputA >= inputD >= inputC >= inputB):
        print("The sorted list is:", inputA, inputD, inputC,inputB)
    
elif (inputB >= inputA) and (inputB >= inputC) and (inputB >= inputD) :
    if (inputB >= inputA >= inputC >= inputD):
        print("The sorted list is:", inputB, inputA, inputC, inputD)
    elif (inputB >= inputC >= inputA >= inputD):
        print("The sorted list is:", inputB, inputC, inputA, inputD)
    elif (inputB >= inputA >= inputD >= inputC):
        print("The sorted list is:", inputB, inputA, inputD, inputC)
    elif (inputB >= inputD >= inputA >= inputC):
        print("The sorted list is:", inputB, inputD, inputA, inputC)
    elif (inputB >= inputC >= inputD >= inputA):
        print("The sorted list is:", inputB, inputC, inputD, inputA)
    elif (inputB >= inputD >= inputC >= inputA):
        print("The sorted list is:", inputB, inputD, inputC, inputA)

elif (inputC >= inputA) and (inputC >= inputB) and (inputC >= inputD)  :
    if (inputC >= inputA >= inputB >= inputD):
        print("The sorted list is:", inputC, inputA, inputB, inputD) 
    elif (inputC >= inputB >= inputA >= inputD):
        print("The sorted list is:", inputC, inputB, inputA, inputD) 
    elif (inputC >= inputA >= inputD >= inputB):
        print("The sorted list is:", inputC, inputA, inputD, inputB) 
    elif (inputC >= inputD >= inputA >= inputB):
        print("The sorted list is:", inputC, inputD, inputA, inputB) 
    elif (inputC >= inputB >= inputD >= inputA):
        print("The sorted list is:", inputC, inputB, inputD, inputA) 
    elif (inputC >= inputD >= inputB >= inputA):
        print("The sorted list is:", inputC, inputD, inputB, inputA) 

elif (inputD >= inputA) and (inputD >= inputB) and (inputD >= inputC) :
    if (inputD >= inputA >= inputB >= inputC):
        print("The sorted list is:", inputD, inputA, inputB, inputC) 
    elif (inputD >= inputB >= inputA >= inputC):
        print("The sorted list is:", inputD, inputB, inputA, inputC)
    elif (inputD >= inputA > inputC >= inputB):
        print("The sorted list is:", inputD, inputA, inputC, inputB)
    elif (inputD >= inputC >= inputA >= inputB):
        print("The sorted list is:", inputD, inputC, inputA, inputB)
    elif (inputD >= inputB >= inputC >= inputA):
        print("The sorted list is:", inputD, inputB, inputC, inputA)
    elif (inputD >= inputC >= inputB >= inputA):
        print("The sorted list is:", inputD, inputC, inputB, inputA)
