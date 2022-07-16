a = int(input('Please enter a HUGE number: '))

z = a/60
y = a%60
x = a/3600
w = a%3600
v = a/86400
u = a%86400
t = w/60
s = w%60
r = u/3600

print((str(int(v))) + ' : '+ (str(int(r))) + ' : ' + str(int(t)) + ' : ' + str(int(s)))

#if a <= 59:
#    print(str(int(a)) + ' seconds')
#elif a == 60:
#    print(str(int(z)) + ' minute')
#elif 60 < a < 3600:
#    print(str(z) + ' minutes ' + str(int(y)) + ' seconds ')
#elif 61 <= a <= 119:
#    print(str(int(z)) + ' minute ' + str(int(y)) + ' seconds ')
#elif 3601 <= a <= 3660:
#    print((str(int(x))) + ' hour ' + str(int(t)) + ' minute ' + str(int(s)) + ' seconds ') 
#elif 3661 <= a <= 7200:    
#    print((str(int(x))) + ' hour ' + str(int(t)) + ' minutes ' + str(int(s)) + ' seconds ') 
#elif 7201 <= a <= 86400:    
#    print((str(int(x))) + ' hours ' + str(int(t)) + ' minutes ' + str(int(s)) + ' seconds ')     
#elif 86401 <= a <= 90000:
#    print((str(int(v))) + ' day '+ (str(int(r))) + ' hours ' + str(int(t)) + ' minutes ' + str(int(s)) + ' seconds ')
#elif 90001 <= a <= 93600:#
#    print((str(int(v))) + ' day '+ (str(int(r))) + ' hour ' + str(int(t)) + ' minutes ' + str(int(s)) + ' seconds ')
#elif 93601 <= a <= 172800:
#    print((str(int(v))) + ' day '+ (str(int(r))) + ' hours ' + str(int(t)) + ' minutes ' + str(int(s)) + ' seconds ')
#elif 172801 <= a <= 604800:
#    print((str(int(v))) + ' days '+ (str(int(r))) + ' hours ' + str(int(t)) + ' minutes ' + str(int(s)) + ' seconds ')