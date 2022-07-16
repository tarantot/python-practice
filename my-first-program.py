#A primitive calculator V1

from colorama import init
from colorama import Fore, Back, Style

print(Fore.BLACK)
print(Back.YELLOW)
a = float (input ("Please enter the 1st number: "))

print(Back.CYAN)
what = input ("What would you like to do? (+, -, *, /): ")

print(Back.YELLOW)
b = float (input ("Please enter the 2nd number: "))

print(Back.RED)
if  what == "+":
    c = a + b
    print ("Your result: " + str(c))
elif what == "-":
    c = a - b
    print ("Your result: " + str(c))
elif what == "*":
    c = a * b
    print ("Your result: " + str(c))
elif what == "/":
    c = a / b
    print ("Your result: " + str(c))

else:
    print ("Please choose a correct action!") 