from random import randint

a = int( input ("Введите нижнюю границу: "))
b = int( input ("Введите верхнюю границу: "))
c = int( input ("Сколько ты хочешь? "))
 
list = []

for i in range(c):
    list.append(randint(a, b))

print(list)

like = str("Y") or str("N")
like = str( input( "Доволен? Y / N "))


if like == str("Y"):
    print ("Прелестно!")

if like == str("N"):
    d = int( input ( "Ну и шо тебе не нравится? Введите число от 0 до " + str(c-1) + ": "))
    if d > c:
        print( "ERROR" )
    else:
        e = int( input ( "Что же взамен? "))
        del list[d] 
        list.insert(d, e)
        print(list)
        print(str( input( "Доволен? Y / N ")))
    

        

#like == "Y"
#while True:
    #print("Прелестно!")
