from random import randint
import math

a = int( input ("Введите нижнюю границу: "))
b = int( input ("Введите верхнюю границу: "))
c = int( input ("Сколько ты хочешь? "))
 
l = []

for i in range(c):
    l.append(randint(a, b)) 
print ('l = {} - созданный список'.format(l))    

def func(x):
    if x > 7:
        return 1
    else:
        return 0

l_ = filter(func, l)
l_ = list(l_)
print ('l_ = {} - Элементы >7'.format(l_))# homework-for-Feb-3
