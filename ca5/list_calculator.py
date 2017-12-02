import math

def get_algor():
    l = ['A','S','M','D','E','Q','F','L','P','N','X']
    s = ''
    while s not in l:
        s = input("Select (A)dd,(S)ubtract,(M)ultiply,(D)ivide,(E)xponential,S(Q)uare Root,(F)actorial,(L)og,(P)erimeter of circle,Si(N),E(X)it: ").upper()
    return (s)

def get_inputlist():
   il = [int(x) for x in input("Enter list of numerics(comma separated): ").split(',')]
   return(il)

s = ''

while s != 'X':
    s = get_algor()
    if s == 'X':
        exit()
        
    a = get_inputlist()

    if s in ['A','S','M','D','E']:
        b = get_inputlist()
        print('List A = ',a)
        print('List B = ',b)
    else:
        print('List = ', a)


    if s == 'A':
        print('Add the Lists: ', list(map(lambda x,y:x+y, a,b)))
    elif s == 'S':
        print('Subtract the Lists: ', list(map(lambda x,y:x-y, a,b)))
    elif s == 'M':
        print('Multiply the Lists: ', list(map(lambda x,y:x*y, a,b)))
    elif s == 'D':
        print('Divide the Lists: ', list(map(lambda x,y:x/y, a,b)))
    elif s == 'E':
        print('Exponential of the Lists: ', list(map(lambda x,y:x**y, a,b)))
    elif s == 'Q':
        print('Square root of the list: ', list(map(lambda x: x**0.5, a)))
    elif s == 'F':
        print('Factorial of the list: ', list(map(lambda x: math.factorial(x), a)))
    elif s == 'L':
        print('Log of the list: ', list(map(lambda x: math.log10(x), a)))
    elif s == 'P':
        print('Perimeter of a circle where the radian is the list: ', list(map(lambda x: 2*math.pi*x, a)))
    elif s == 'N':
        print('Sine of the list: ', list(map(lambda x: math.sin(x), a)))
    else:
        print('Invalid Function')
