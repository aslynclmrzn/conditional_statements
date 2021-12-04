# Program 2: Addition Trainer
import random
from random import randint
import shutil
columns = shutil.get_terminal_size().columns
class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    
print(bcolors.HEADER + "WELCOME TO ADDITION TRAINER".center(columns) + bcolors.ENDC)

score = 0

# Create a program that automatically generate two random numbers to add (0 to 99)
for i in range (0,10):
    number1 = randint(0,99)
    number2 = randint(0,99)
    operators = ['+']
    operation = random.choice (operators) 
# The program will ask the user 10 addition operation
    problemSet = print(f"What is {number1} {operation} {number2}?")
    usersAnswer = (input("Enter your answer: "))
    answer = int(usersAnswer)
    solution = number1 + number2
# Let the user answer and evaluate if the user has the correct answer
    if (answer == solution):
        score = score + 1
        print (bcolors.OKGREEN + "Correct!" + bcolors.ENDC)
        print ()
    else:
        print (bcolors.FAIL + "Incorrect!" + bcolors.ENDC)
        print (f"The correct answer is {solution}.")
        print ()
# Description
if score >=6 and score <=10:
    print ("Very Good!")
elif score <=6 and score >=1:
    print ("Good Job! Keep it up.")
elif score == 0:
    print ("Try again.")
#Display the result summary of the 10 operations (ex 9/10)
print (f"Your score is {score}/10!")