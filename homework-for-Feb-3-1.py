from random import randint
import math

a = int( input ("Введите нижнюю границу: "))
b = int( input ("Введите верхнюю границу: "))
c = int( input ("Сколько ты хочешь? "))
 
l = []
l2 = []
l_2 = []
l3 = []
l_3 = []
l_n = []

for i in range(c):
    l.append(randint(a, b))
    
for i in l:    
    l2.append(i**2)

for i in l:    
    l_2.append(pow(i,-2))
    
for i in l:    
    l3.append(i**3)

for i in l:    
    l_3.append(pow(i,-3))

    
print ('l = {} - созданный список\nl2 = {} - элементы списка в квадрате\nl_2 = {} - элементы списка в -2 степени\nl3 = {} - элементы списка в кубе\nl_3 = {} - элементы списка в -3 степени'.format(l, l2, l_2, l3, l_3))

like = str("Y") or str("N")
like = str( input( "Хотите продолжить? Y / N "))

while like == str("Y"):
    n = float(input("В какую степень? Введите число: ")) 
    for i in l:
        l_n.append(pow(i, n))
    
    print((l_n)" - элементы списка в " + str(n) + " степени")
    like = str( input( "Ещё? Y / N "))
    
if like == str("N"):
    print ('Ну вот и славно')