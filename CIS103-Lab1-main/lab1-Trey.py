# Lab 1: Getting Started with Python
# CIS 103: Introduction to Programming
# Instructor: Md Ali
# Student Name: Trey Wallace # Date: 9/1/2024
# Description:
# This script prints a personalized greeting message to the user.
# and demonstrates the use of variables and basic data types.
# --------------------------------------------------------

# name and age as a variable instead of a function
#feels easier to manage

name = input("Enter your name: ")
age = int(input("Enter your age:"))

#Calculates when someone was born
def whatyear():
    current_year = 2024
    birth_year = current_year - age
    return birth_year

#The actual function
def personalgreeting():
    return print(f"Hello, {name}! You were born in {whatyear()} and you are {age} years old.")
    



if __name__ == "__main__":
    personalgreeting()