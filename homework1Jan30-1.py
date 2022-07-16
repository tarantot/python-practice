a = float( input( "Введите первое число: "))
b = float( input( "Введите второе число: "))
c = float( input( "Введите третье число: "))

if a == b:
	print( "А если так?")
	if a+c > b-c:
		print( str(a+c) + ">" + str(b-c))
	elif a+c < b-c:
		print( str(a+c) + "<" + str(b-c))

elif a > b:
	print( "Свершилось!")

elif b > a:
	print( "Да ну!")	