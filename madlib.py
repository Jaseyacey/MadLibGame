# random is randomly selecting a sentence
import random
f = open('madlibs.txt', 'r')
# Reading the lines to find the word to be replaced
madlibs = f.readlines()
# This is calling the text file
madlib = random.choice(madlibs)
# Asking for user input
noun = input("Enter a noun: ")
# Replacing the word Blank with the user input which is noun
madlib = madlib.replace("blank", noun)

print(madlib)
