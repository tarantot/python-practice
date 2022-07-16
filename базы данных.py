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

dish1 = str(input('What\'s your favorite liquid dish? '))
dish2 = str(input('What\'s your favorite main dish? '))
print('Today you will have some ' + dish1 + ' and ' + dish2 +' for dinner!')