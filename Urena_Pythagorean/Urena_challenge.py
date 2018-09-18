a = int(input("Please enter side a: "))
b = int(input("Please enter side b: "))
c = int(input("Please enter side c: "))
d = (a**2)
e = (b**2)
f = (c**2)

if (f == (d + e)) :
    print("You have a right triangle.")
elif ((d + e) < f ) :
    print("You have an obtuse triangle.")
elif ((d + e) > f ) :
    print("You have an acute triangle.")
else :
    print("Oops! Try an integer")