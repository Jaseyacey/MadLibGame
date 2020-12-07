import random

f = open('madlibs.txt', 'r')

madlibs = f.readlines()

madlib = random.choice(madlibs)

noun = input("Enter a noun: ")

madlib = madlib.replace("blank", noun)

print(madlib)
