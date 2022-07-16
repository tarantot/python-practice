#ФУНКЦИИ
def display(message): #- вызов функции
    print(message)
def give_me_five():
    five = 5
    return five
def ask_yes_no(question):
    '''Are you dumb?'''
    response = None
    while response not in ('Y','N'):
        response = input(question).upper()
    return response
display('You\'ve got a message!')
number = give_me_five()
print('Here\'s what "giv_me_five" function returns us: ',number)
answer = ('\nPlease enter \'Y\' or \'N\': ')
print('Thanks for your answer!',answer)
input('Press ENTER to leave')