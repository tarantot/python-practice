#initfile = 'test.txt' - разбивка существующего файла на 3 
#outputfile1 = 'bob.txt'
#outputfile2 = 'sue.txt'
#outputfile3 = 'tom.txt'
#dbfile = open('test.txt',mode='r',encoding='utf_8')
#fl1 = open('bob.txt',mode='w',encoding='utf_8')
#fl2 = open('sue.txt',mode='w',encoding='utf_8')
#fl3 = open('tom.txt',mode='w',encoding='utf_8')
#for line in dbfile:
#    if 'bob' in line:
#        fl1.write(line)
#    if 'sue' in line:
#        fl2.write(line)
#    if 'tom' in line:
#        fl3.write(line)
#dbfile.close()
#print(dbfile['sue']['name'])
#for bob in handle:
#    print(['bob']['name']) 
#handle.close()

initfile = 'test.txt'
dbfile = open('test.txt',mode='a',encoding='utf_8')
for line in dbfile:
    if name in line:
        dbfile.write('Bob Robert')
dbfile.close()
    