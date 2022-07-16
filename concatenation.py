name = input ("Please enter your name: ")
surname = input ("Please enter your surname: ")
age = input ("Please enter your age: ")
sex = input ("sex: M / F: ")

if sex == "M":
    print ("Hello, Mr. "  + name + " " + surname + "!" + " " + "You are already " + age + " years old, that's cool! ;-)")
elif sex == "F":
    print ("Hello, Ms. / Mrs. " + name + " " + surname + "!" + " " + "You are already " + age + " years old, that's cool! ;-)")
else:
    print ("Are you nuts, " + name + surname + "?")