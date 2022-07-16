a = float( input( "Введите первое число: "))
b = float( input( "Введите второе число: "))
c = float( input( "Введите третье число: "))

while (a <= b):
    print ("Значение " + str(a) + ", пока что нет")
    a = a + c    

print ("Дождались!" + str(a+c))