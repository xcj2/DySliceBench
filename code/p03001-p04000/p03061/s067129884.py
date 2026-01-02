n = int(input())
a = [int(x) for x in input().split()]

def gcd(x, y):
    #print('gcd({0},{1})'.format(x,y))
    if (y==0):
        return x
    else:
        return gcd(y, x%y)

def gcd_left(i):
    #print('gcd_left({0})'.format(i))

    if i<=-1:
        return 0
    else:
        if l[i]:
            return gcd(gcd_left(i-1), a[i])
        else:
            l[i] = gcd( gcd_left(i-1), gcd_right(i+1))


def gcd_right(i):
    #print('gcd_left({0})'.format(i))
    
    if i>=n:
        return 0
    else:
        return gcd( a[i], gcd_right(i+1))

def gcd_left_update(ls, i):
    #print('gcd_left({0})'.format(i))

    if i<0:
        return 0
    elif i==0:
        return a[i]
    else:        
        return gcd(ls[i-1], a[i])


def gcd_right_update(ls, i):
    #print('gcd_right({0})'.format(i))
    
    if i>=n:
        return 0
    elif i==n-1:
        return a[i]
    else:
        return gcd( a[i], ls[i+1])

def gcd_excepts(i):
    #print('gcd_excepts({0})'.format(i))
    return gcd( gcd_left(i-1), gcd_right(i+1))

def gcd_excepts2(i):
    #print('gcd_excepts2({0})'.format(i))
    left = 0
    right = 0
    if i-1<0:
        left = 0
    else:
        left = l[i-1]
    
    if i+1>=n:
        right = 0
    else:
        right = r[i+1]
        
    return gcd( left, right )

l = [None for i in range(n)]
for i in range(n):
    l[i] = gcd_left_update(l,i)

r = [None for i in range(n)]
for i in reversed(range(n)):
    r [i] = gcd_right_update(r,i)
    
m = [gcd_excepts2(i) for i in range(n)]

print(max(m))