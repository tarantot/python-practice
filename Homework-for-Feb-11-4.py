a = str(input('Please enter a sentence: '))
b = str(input('Please enter a letter to search: '))
count = a.count(b)
if count == 0:
    print('ERROR')
else:
    print('There are ' + str(int(count)) + ' letters ' + str(b) + ' in your sentence. \nThank you!')