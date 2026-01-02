


t = int(input())
qs=[list(map(int,input().split())) for i in range(t)]

def computeGCD(x, y):
   while(y):
       x, y = y, x % y
   return x

def aprime(a,b,c,d):
    app = a%b
    return(c+d-b - (c-app)%(d-b))


def ans(a,b,c,d):
    if d < b or a<b or (a%b > c and c<b):
        return('No')
    elif b == d or c > b:
        return('Yes')
    elif aprime(a,b,c,d) < b:
        return('No')
    else: return (ans2(aprime(a,b,c,d),b,c,d))

def ans2(a,b,c,d):
    b2 = b % (d-b)
    gcdbbd = abs(computeGCD(b2,b-d))
    aa = a - ((a-c)//gcdbbd)*gcdbbd
    if aa == c: aa = c+ gcdbbd
    if aa >= b: return('Yes')
    else: return('No')

for q in qs:
    print (ans(*q))

