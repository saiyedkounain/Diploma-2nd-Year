#Quadratic Equation
#bsq-4ac
import math
a=int(input("Enter a: "))
b=int(input("Enter b; "))
c=int(input("Enter c: "))
d=(b**2)-(4*a*c)
if d == 0:
    r1=-b/2*a
    print("The roots are real and equal",r1)
elif d > 0:
    r1= -b+(d**0.5)/2*a
    r2= -b-(d**0.5)/2*a
    print("The roots are real and distinct", r1,r2)
else:s
    print("The roots are imaginary")
