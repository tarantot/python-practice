print("Введите значени А")
a = int(input())
print("Введите значени Б")
b = int(input())
print("Введите значени C")
c = int(input())
if a>b:
    print("Свершилось")
if a<b:
    print("Да ну!")
if a==b:
    print("А если так?")
    a = a+c
    b = b-c
    print("a+c=", a)
    print("b-c=", b)
    if a>b:
        print("Свершилось")
    if a<b:
         print("Да ну!")