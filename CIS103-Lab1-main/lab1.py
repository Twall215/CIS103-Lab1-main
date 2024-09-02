# Lab 1: Getting Started with Python
# CIS 103: Introduction to Programming
# Instructor: Md Ali
# Student Name: Trey Wallace # Date: 9/1/2024
# Description:
# This script prints a personalized greeting message to the user.
# and demonstrates the use of variables and basic data types.
# --------------------------------------------------------
#functions to ask the user their name and age
def name():
    x = input("Enter your name: ")
    return x

def age():
    num = int(input("Enter your age:"))
    return num


def WusYaName():
    return print(f"Your name is {name()} and you are {age()} years old")
    



if __name__ == "__main__":
    WusYaName()