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
    guess = input('\nPlease enter a letter: ')
    guess = guess.upper()
used.append(guess)

if wrong == max_wrong:
    print(hangman[wrong])
    print('\nYou were hanged! What a disaster.')
else:
    print('\nYou won!')
print('\nThe word is '+word+'! \nDo you know which country it is the capital of? ;-)')
input('\n\nPress ENTER to leave')