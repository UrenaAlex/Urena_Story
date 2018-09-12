"""
Write a program what will take a number (Integers only) and
return a statement that will let the user know if it is even or odd
"""

x = int(input("Hello, I will tell you if a number is even or odd, please enter a number. "))

if (x%2 == 0) :
    print("You have an even number. ")
elif (x % 2 == 1) :
    print("You have an odd number. ")
else :
    print("Oops! looks like you didnt enter a whole number!")