dictchinese = {'zero':'零','one':'一','two':'二','three':'三','four':'四','five':'五','six':'六','seven':'七','eight':'八','nine':'九'}
print('\nChinese numbers (simplified): ')
for key, value in dictchinese.items():    
    print(key, 'is', value)
    
dictthai = {'zero':'๐','one':'๑','two':'๒','three':'๓','four':'๔','five':'๕','six':'๖','seven':'๗','eight':'๘','nine':'๙'}
print('\nThai numbers: ')
for key, value in dictthai.items():
    print(key, 'is', value)
    
dicthindi = {'zero':'०','one':'१','two':'२','three':'३','four':'४','five':'५','six':'६','seven':'७','eight':'८','nine':'९'}
print('\nHindi numbers: ')
for key, value in dictthai.items():
    print(key, 'is', value)
    
newdict = {}
print('\nNEW DICTIONARY:\n')
for key in dictchinese:
    newdict[key] = [d[key] for d in (dictchinese, dictthai, dicthindi)] 
print(newdict)