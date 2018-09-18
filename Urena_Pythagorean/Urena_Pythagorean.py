name = input("Hello user! What is your name? ")

print("Nice to meet you " + name + "! Please enter two values for the length of the legs of a right triangle, I will give you it's hypotenuse. ")

a = float(int(input("Please enter a value for leg 'a': ")))

b = float(int(input("Please enter a value for leg 'b': ")))

c = (((a**2)+(b**2))**.5)

print("Your hypotenuse length is: " + str(c))