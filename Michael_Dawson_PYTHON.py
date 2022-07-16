#import datetime - количество дней между сегодняшней и введённой датой
#a = input('Введите дату Вашего рождения в формате (гггг-мм-дд): ')
#z = int(input('Введите Ваш вес: '))
#a = a.split('-')
#aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
#bb = datetime.date.today()
#cc = abs(aa-bb)
#dd = str(cc*86400)
#print('На сегодня Ваш земной возраст - ' + str(dd.split()[0]) + ' секунд!\n А знаете ли Вы, что на Юпитере Вы весили бы ' + str(z*2.36538461538462)[:5] + ' килограмм, a Ваш возраст составлял бы ' + str(cc/11.805)[:3] + ' дней!\nА вот на Луне мечтали бы оказаться те, кто хочет похудеть, - ведь их вес там был бы приверно в 6 раз меньше (в частности Ваш составлял бы ' + str(z/6.05555)[:4] + ' килограммов).\nХорошая идея, не так ли?\nА вот на Солнце, каждый - тяжеловес: ещё бы, с массой ' + str(z*27,95918367346939)[:5] + '! Правда, ненадолго...')

#print('Here', end=' is ') - ещё один способ вывода строк
#print('it!')

#print('\tHere', end=' is it!') # - снос строки вправо

#print('\aHello World!') - системный звук вместе с строкой вывода

#phrase = str(input('Copy and paste the following sentence: \"If you\'re happy and you know it - clap your hands!\" :'))
#print(phrase.replace('happy','ugly') + '\nCan\'t you just copypaste it correcty, huh?!') - замена одного из элементов для вывода

#dish1 = str(input('What\'s your favorite liquid dish? '))
#dish2 = str(input('What\'s your favorite main dish? '))
#print('Today you will have some ' + dish1 + ' and ' + dish2 +' for dinner!')

#from random import randint
#import math
#print('\t\t\tWELCOME TO THE GAME \'GUESS A NUMBER\'\n\n\tThe randomizer will generate a number in rabge 1-100, and you try to guess it! Ready?\nLet\'s go!')
#thenumber = randint(0,100)
#guess = int(input('Please enter your number: '))
#tries = 1
#while thenumber != guess:
#    if guess > thenumber:
#        print('It\'s lower...')
#        tries += 1
#    else:
#        print('It\'s higher...')
#        tries += 1
#    guess = int(input('Please enter your number: '))
#if thenumber == guess:
#    print('Congratulations! You\'re right - the number is '+str(thenumber)+'!')
#    if tries == 1:
#        print('It took you just a single attempt to guess! You must be a genius!')
#    else:
#        print('It took you just '+str(tries)+' attempts to guess, you\'re a lucky man!')

#from random import randint
#print('\t\tДОБРО ПОЖАЛОВАТЬ В ИГРУ \"ПИРОЖОК-СЮРПРИЗ\"')
#answer = str(input('Хотите попытать свою удачу? Y / N '))
#nachinka = randint(0,4)
#while answer == 'Y':
#    if nachinka == 1:
#        print('Сегодня Вам повезло полакомиться пирожком с яблоками. Приятного аппетита!')
#    elif nachinka == 2:
#        print('Сегодня Вам повезло полакомиться пирожком со сливами. Приятного аппетита!')
#    elif nachinka == 3:
#        print('Сегодня Вам повезло полакомиться пирожком с маком. Приятного аппетита!')
#    elif nachinka == 4:
#        print('Сегодня Вам повезло полакомиться пирожком с вишнями. Приятного аппетита!')
#    else:
#        print('Пирожок с тестом ждёт Вас! Ха-ха')
#    answer = str(input('Хотите попытать свою удачу? Y / N '))
#    nachinka = randint(0,4)
#if answer == 'N':
#    print('Ну как, вкусненько?')

#from random import randint
#print('\t\tПОДБРОСИМ МОНЕТКУ?')
#coin = randint(0,1)
#flip = 1
#flip_tails = 0
#flip_heads = 0
#while flip <= 100:
#    if coin == 0:
#        coin = 'решка'
#        flip_tails+=1
#    else:
#        coin = 'орёл'
#        flip_heads+=1
#    coin = randint(0,1)
#    flip+=1
#if flip == 101:
#    print(str(flip_heads)+' раз выпал орёл, '+str(flip_tails)+' раз выпала решка!')

#print('Let\'s count! ')
#for i in range(10): - #ряд чисел от 0 до 9
#    print(i,end=' ')
#print('\n\nEnlist the multiples of five: ')
#for i in range(0,50,5): - #ряд чисел от 0 до 45 с шагом 5
#    print(i,end=' ')
#print('\n\nLet\'s count in the reverse order: ')
#for i in range(10,0,-1): - #ряд чисел от 9 до 0 с шагом -1
#    print(i,end=' ')
#input('\n\nPress ENTER to leave the program')

#inventory = () #- создание кортежа
#if not inventory:
#    print('You\'re unarmed!')
#input('\nPress ENTER to continue')
#inventory = ('sword','armor','shield','healing balsam')
#print('\nThe tuple inventory is:\n')
#print(inventory)
#print('\nSo, here are all your avilable items:')
#for item in inventory:
#    print(item)
#print('\nFor now you have ' + str(len(inventory)) + ' items')
#input('\nPress ENTER to continue')
#if 'healing balsam' in inventory:
#    print('You\'re gonna live long and fight well!')
#index = int(input('\nPlease enter the index of an item in your inventory: '))
#print('With the index ' + str(index) + ' you have ' + inventory[index] +  '!')
#input('\nPress ENTER to continue')
#
#chest = ('Gold','Gems') #- сцепление кортежей
#print('\nYou\'ve found a chest! Here\'s what inside: ')
#for item in chest:
#    print(item)
#print('You\'ve just added these items to your inventory!')
#inventory += chest
#print('\nHere\'s what you totally have now: ')
#for item in inventory:
#    print(item)
#input('\nPress ENTER to leave')

#import random 
#- анаграмма: угадать рандомно выбранное слово из списка по буквам
# create a sequence of words to choose from
#WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
#word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
#correct = word
# create a jumbled version of the word
#jumble =""
#while word:
#    position = random.randrange(len(word))
#    jumble += word[position]
#    word = word[:position] + word[(position + 1):]
# start the game
#print(
#"""
#           Welcome to Word Jumble!
#        
#   Unscramble the letters to make a word.
#(Press the enter key at the prompt to quit.)
#"""
#)
#print("The jumble is:", jumble)
#guess = input("\nYour guess: ")
#while guess != correct and guess != "":
#    print("Sorry, that's not it.")
#    guess = input("Your guess: ")
#if guess == correct:
#    print("That's it!  You guessed it!\n")
#print("Thanks for playing.")
#input("\n\nPress the enter key to exit.")

#Программа которая принимает текст ввода и выводит его в обратной последовательности
#line = str(input('Just type something, go ahead: '))
#input('\nPress Enter to see a miracle...')
#print('Here it comes! ' + line[::-1]) # - вывод строки в обратном порядке

#АРСЕНАЛ ГЕРОЯ 3.0
#inventory = ['sword','armor','shield','healing balsam']
#print('\nThis is your inventory: \n')
#for item in inventory:
#    print(' - ' + item)
#print('\nNow you have ' + str(len(inventory)) + ' items available!')
#input('\nPress ENTER to continue')
#if 'healing balsam' in inventory:
#    print('\nYou\'re gonna live long and fight well!')
#index = int(input('\nEnter the index of one of your available items: '))
#print('\nYou have ' + inventory[index-1] + ' with the index ' + str(index) + '!')
#input('\nPress ENTER to continue')
#chest = ['gold','gems']
#print('\nCongratulations, you found a chest! Here\'s what inside: ')
#for item in chest:
#    print(' - ' + item)
#inventory += chest
#print('\nSo now you totally have: ')
#for item in inventory:
#    print(' - ' + item)
#input('\nPress ENTER to continue')
#print('\nYou exchanged your sword for a crossbow! Your new inventory is: ')
#inventory[0] = 'crossbow'
#for item in inventory:
#    print(' - ' + item)
#input('\nPress ENTER to continue')
#print('You bought a magic crystal to see the future for gold and gems! Now your inventory is: ')
#inventory[4:6] = ['magic crystal']
#for item in inventory:
#    print(' - ' + item)
#input('\nPress ENTER to continue')
#print('\nIn a dubious battle your shield was smashed. Here\'s what you have left: ')
#del inventory[2]
#for item in inventory:
#    print(' - ' + item)

#HANGMAN
import random
hangman = (
        '''
     ______/|\______''',
'''         ________
            |      
            |       
            |      
            |      
            |
            |
            |
            |
     ______/|\______''',
'''         ________
            |      |
            |      | 
            |      
            |      
            |
            |
            |
            |
     ______/|\______''', 
'''         ________
            |      |
            |      | 
            |      O
            |    
            |      
            |
            |
            |
     ______/|\______''',
'''         ________
            |      |
            |      | 
            |      O
            |      |
            |      
            |
            |
            |
     ______/|\______''',
'''         ________
            |      |
            |      | 
            |      O
            |    __|__
            |      
            |
            |
            |
     ______/|\______''',
'''         ________
            |      |
            |      | 
            |      O
            |    __|__
            |      |
            |
            |
            |
     ______/|\______''',
'''         ________
            |      |
            |      | 
            |      O
            |    __|__
            |      |
            |     / \
            |
            |
     ______/|\______''')
max_wrong = len(hangman) - 1
capitals = ['KABUL', 'TIRANA','ALGIERS','ANDORRA-LA-VELLA','LUANDA',"SAINT JOHNS"'BUENOS-AIRES','YEREVAN','CANBERRA','VIENNA','BAKU','NASSAU','MANAMA','DHAKA',"BRIDGETOWN",'MINSK','BRUSSELS','BELMOPAN','PORTO-NOVO','THIMPHU','SUCRE','SARAJEVO','GABORONE','BRASILIA','BANDAR SERI BEGAWAN','SOFIA','OUAGADOUGOU','BUJUMBURA','PRAIA','PHNOM PENH','YAOUNDE','OTTAWA','BANGUI','NDJAMENA','SANTIAGO','BEIJING','BOGOTÁ','MORONI','KINSHASA','SAN JOSE','YAMOUSSOUKRO','ZAGREB','HAVANA','NICOSIA','PRAGUE','COPENHAGEN','DJIBOUTI CITY','ROSEAU','SANTO DOMINGO','QUITO','CAIRO','SAN SALVADOR','MALABO','ASMARA','TALLINN','MBABANE','ADDIS ABABA','PALIKIR','SUVA','HELSINKI','PARIS','LIBREVILLE','BANJUL','TBILISI','BERLIN','ACCRA','ATHENS','SAINT-GEORGES','GUATEMALA CITY','CONAKRY','BISSAU','GEORGETOWN','PORT-AU-PRINCE','TEGUCIGALPA','BUDAPEST','REYKJAVIK','NEW DELHI','JAKARTA','TEHRAN','BAGHDAD','DUBLIN','JERUSALEM','ROME','KINGSTON','TOKYO','AMMAN','NUR-SULTAN','NAIROBI','SOUTH TARAWA','PRISTINA','KUWAIT CITY','BISHKEK','VIENTIANE','RIGA','BEIRUT','MASERU','MONROVIA','TRIPOLI','VADUZ','VILNIUS','LUXEMBOURG','ANTANANARIVO','LILONGWE','KUALA LUMPUR','MALE','BAMAKO','VALLETTA','MAJURO','NOUAKCHOTT','PORT LOUIS','MEXICO CITY','CHISINAU','MONACO','ULAANBAATAR','PODGORICA','RABAT','MAPUTO','NAY PYI TAW','WINDHOEK','YAREN DISTRICT','KATHMANDU','AMSTERDAM','WELLINGTON','MANAGUA','NIAMEY','ABUJA','PYONGYANG','SKOPJE','OSLO','MUSCAT','ISLAMABAD','NGERULMUD','EAST JERUSALEM','PANAMA CITY','PORT MORESBY','ASUNCION','LIMA','MANILA','WARSAW','LISBON','DOHA','BRAZZAVILLE','BUCHAREST','MOSCOW','KIGALI','BASSETERRE','CASTRIES','KINGSTOWN','APIA','SAN MARINO','SAO TOME','RIYADH','DAKAR','BELGRADE','VICTORIA','FREETOWN','SINGAPORE','BRATISLAVA','LJUBLJANA','HONIARA','MOGADISHU','CAPE TOWN','SEOUL','JUBA','MADRID','COLOMBO','KHARTOUM','PARAMARIBO','STOCKHOLM','BERN','DAMASCUS','DUSHANBE','DODOMA','BANGKOK','DILI','LOME','NUKUALOFA','PORT OF SPAIN','TUNIS','ANKARA','ASHGABAT','FUNAFUTI','KAMPALA','KIEV','ABU DHABI','LONDON','WASHINGTON D.C.','MONTEVIDEO','TASHKENT','PORT VILA','VATICAN CITY','CARACAS','HANOI','SANAA','LUSAKA',
'HARARE']
word = random.choice(capitals)
if len(word) < len(hangman):
    hangman[(len(hangman) - len(word)):]
so_far = str('_' * len(word))
wrong = 0
used = []
print('''\n\t\t\tWELCOME TO THE GAME \'HANGMAN\'!
\t\t\tYOU NEED TO GUESS A CAPITAL CITY.
\t\t\tYOU HAVE 7 ATTEMPTS. WISH YOU LUCK!\n''') 
guess = input('\nPlease enter a letter: ')
guess = guess.upper()
while guess in used:
    print('\nYou already used this letter! Please enter a different one. ')
    guess = ('\nPlease enter a letter: ')
    guess = guess.upper()
used.append(guess)

if guess in word:
    print('\nYES! The letter ' + guess + ' is in the word!')
    new = ''
    for i in range(len(word)):
        if guess == word[i]:
            new+=guess
        else:
            new+=so_far[i]
    so_far = new
else:
    print('\nUnfortunately, there is no letter '+guess+' in this word!') 
    wrong+=1

while wrong < max_wrong and so_far != word:
    print(hangman[wrong])
    print('\nYou have already used the following letters: ')
    for u in used:
        print(' - '+u)
    print('\nFor now your word is ' + so_far)
    if wrong+=1:
        break

if wrong == max_wrong:
    print(hangman[wrong])
    print('\nYou were hanged! What a disaster.')
else:
    print('\nYou won!')
print('\nThe word is '+word+'! \nDo you know which country it is the capital of? ;-)')
input('\n\nPress ENTER to leave')



