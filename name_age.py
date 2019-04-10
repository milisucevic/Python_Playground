"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""
from datetime import datetime
name = input('What is your name? \n')
age = int(input('How old are you? \n'))
hundred = int((100-age) + datetime.now().year)
print ('Hello %s. You are %s years old. You will turn 100 years old in %s.' % (name, age, hundred))
