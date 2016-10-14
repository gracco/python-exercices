#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
import datetime

name =  input("Please enter your name:")
age = int(input("Please enter your age:"))

now = datetime.datetime.now()
actual_year = now.year
year_born = actual_year - age
age_hundred = year_born + 100

print('{} you gonna be 100 years old in {}'.format(name, age_hundred))
