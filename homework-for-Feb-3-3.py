from random import randint
import math

a = int( input ("Введите нижнюю границу: "))
b = int( input ("Введите верхнюю границу: "))
c = int( input ("Введите количество элементов списка: "))
 
l1 = []
l2 = []
l3 = []

for i in range(c):
    l1.append(randint(a, b))
    l2.append(randint(a, b))
    
for x in l1:
    if x in l3:
        continue
    for y in l2:
        if x == y:
            l3.append(x)
            break
   
print ('l1 = {} - первый созданный список\nl2 = {} - второй созданный список\nl3 = {} - список общих элементов'.format(l1, l2, l3))