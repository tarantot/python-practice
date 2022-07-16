from random import randint

a = int( input ("Введите нижнюю границу: "))
b = int( input ("Введите верхнюю границу: "))
c = int( input ("Сколько ты хочешь? "))
 
numbers = []

for i in range(c):
    numbers.append(randint(a, b))

print(numbers)

like = str("Y") or str("N")
like = str( input( "Доволен? Y / N "))


while like == str("N"):
    d = int( input ( "Ну и шо тебе не нравится? Введите число от 0 до " + str(c-1) + ": "))
    if d > c:
        print( "ERROR" )
    else:
        e = int( input ( "Что же взамен? "))
        del numbers[d] 
        numbers.insert(d, e)
        print(numbers)
    like = str( input( "Доволен? Y / N "))

if like == str("Y"):
    print ("Прелестно!")



    

        

#like == "Y"
#while True:
    #print("Прелестно!")