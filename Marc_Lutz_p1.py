#bob = ['Bob Smith', 42, 30000, 'software']
#sue = ['Sue Jones', 45, 40000, 'hardware']
#print(bob[0], sue[2]) - вывод 1го элемента списка Боб и 3го элемента списка Сью
#print(bob[0].split()[-1]) - вывод 2й части 1го элемента списка Боб
#print(sue[2]*1.45) - повышение 3го элемента списка Сью на коэффициент 1.45
#print(sue[0].split()[0]) - вывод 1й части 1го элемента списка Сью
#people = [bob,sue]
#print(people)
#for person in people:
    #print(people[1][0]) - Sue Jones
    #print(person[0].split()[1]) - Smith / Jones
    #person[2]*=1.3
    #print(person[2]) - вывод 3х элементов каждого из списков умноженных на коэффициент
    #pays = [person[2] for person in people] 
#print(pays)- создание отдельного списка из 3х элементов в обеих списках
    #pays = map((lambda x: x[2]), people)
    #list(pays)
    #sum(person[2] for person in people)
    #print(sum)
#people.append(['Tom Roberts', 50, 1, 'none'])
#print(people[2][0]) - добавление нового списка
#NAME, AGE, PAY, JOB = range(4) 
#print(bob[JOB]) - присвоение итераций каждому из элементов списков с помощью функции range
#def field(record,label):
#    for(fname,fvalue) in record:
#        if fname == label:
#            return fvalue
#        field(bob,'name')
#        field(sue,'pay')
#        for rec in people:
#    print(field(rec,'age'))

#sue = {} #- один из методов создания и наполнения словаря
#sue['name'] = 'Sue Jones'
#sue['age'] = 45
#sue['pay'] = 40000
#sue['job'] = 'hardware' 
#print(sue)

#bob = {} #- один из методов создания и наполнения словаря
#keys = ['name','age','pay','job']
#values = ['Bob Smith',42,30000,'software']
#bob = dict(zip(keys,values))
#print(bob)

#record = {} #- один из методов создания и наполнения словаря
#keys = ['name','age','pay','job']
#record = dict.fromkeys(keys,'?')
#print(record)

#people = [bob,sue]
#for person in people:
#    #print(person['name'], person['pay'], sep=', ') - вывод элементов списка (имя + зарплата) через запятую
#    if person['name'] == 'Sue Jones':
#        print(person['pay'])
#names = [people['name'] for person in people]
#a = list(map((lambda x: x['pay']), people)) #- создание отдельного списка из заданых элементов словарей
#a = sum(person['pay'] for person in people) - cума заданых цифровых элементов списка
#a = [rec['name'] for rec in people if rec['age']>=45] - SQL-подобный запрос вывод имени того чей возраст >=45
#a = [(rec['age']**2 if rec['age']<43 else rec['age']) for rec in people] - SQL-подобный запрос вывода возраста*2 если он <43
#a = ((rec['age']**2 if rec['age']>=45 else rec['age']) for rec in people)
#a = a.__next__() - выводит иной элемент чем тот который задан в строке выше
#print(a)

#bob2 = {'name': {'first': 'Bob', 'last': 'Smith'}, 'age':42, 'job':['software','writing'], 'pay':(40000,50000)} #- словарь со вложенными структурами 
#print(bob2['name']['last'],bob2['name']['first'],sep=' ') #- вывод элементов в заданом(обратном) порядке
#for job in bob2['job']:
#    print(job)
#bob2['job'].append('janitor') #- добавление нового элемента
#print(bob2['job'])

#import pprint #- модуль форматированного вывода
#bob = dict(name='Bob Smith', age=42, pay=30000, job='software')
#sue = dict(name='Sue Jones', age=45, pay=40000, job='hardware')
#db = {}
#db['bob'] = bob
#db['sue'] = sue
#print(db['bob']['name'][-2])
#db['sue']['pay'] = db['sue']['pay']*1.33333333333333 #- метод вывода путём обращения непосредственно к данным словарей, без использования циклов
#print(db['sue']['pay'])
#pprint.pprint(db)

#for key in db:
#    print(key,'=>',db[key]['name']) #- bob => Bob Smith sue => Sue Jones
#    print(db[key]['pay']*1.11)

#for record in db.values():
#    print(record['pay'])

#db['tom'] = dict(name='Tom Hughes', age=38, pay=28000, job='junior') #- добавление нового набора элементов в словарь
#pprint.pprint(db)
#print(len(db)) #- количество списков в словаре
#a = [rec['age'] for rec in db.values()] #- SQL-подобный запрос параметра "возраст" в списках словарей
#print(a)

bob = dict(name='Bob Smith', age=42, pay=30000, job='software')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hardware')
tom = dict(name='Tom Hughes', age=38, pay=28000, job='junior')
db = {}
db['bob']=bob 
db['sue']=sue 
db['tom']=tom
if __name__ == '__main__':
    for key in db:
        print(key,'=>\n',db[key]) #- вывод 3х словарей