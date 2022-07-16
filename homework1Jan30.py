a = int( input( "Введите первое число: "))
b = int( input( "Введите второе число: "))
c = int( input( "Введите третье число: "))
e = int(a + c)
f = int(b - c)

while e == f:	
	input ("Введите числа заново!")

else:
	if a > b:
		print( "Свершилось!")
	elif b > a:
		print( "Да ну!")
	elif a == b:
		print( "А если так?")
		if e > f:
			print (str(e) + " > " + str(f))  
		else:
			print (str(e)) + " < " + str(f))