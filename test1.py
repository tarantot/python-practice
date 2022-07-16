what = input ("What would you like to do? (+ , - , * , /): ")

a = float (input ("Please enter the 1st number: "))
b = float (input ("Please enter the 2nd number: "))

if what == "+"
    c = a + b
    print ("Your result: " + str(c))
elif what == "-"
    c = a - b
    print ("Your result: " + str(c))
elif what == "*"
    c = a * b
    print ("Your result: " + str(c))
elif what == "/"
    c = a / b
    print ("Your result: " + str(c))
else:
    print ("Please choose a correct action!") 