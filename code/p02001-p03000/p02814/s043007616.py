n,m = map(int,input().split())

a = [1]*n
#print(a)
a = [int(s) for s in input().split()]

a_half = [s//2 for s in a]
#print(a)

def check(x):
    while (all(c%2 == 0 for c in x)):
        x = [s//2 for s in x]
        if any(c%2 == 1 for c in x) and any(c%2 == 0 for c in x):
            return 0
        
    
    return 1

def gcd(x,y):
    #print(x,y)
    if(x%y == 0):
        #print(y)
        return y
    else:
        return gcd(y,x%y)


def lcm(x,y):
    return x//gcd(x,y)*y

if(check(a)== 1):
    x = a_half[0]
    for i in range(1,n):
        y = a_half[i]
        x = lcm(x,y)
    if(x > m):
        print(0)
    else:
        res = int((m//x+1)//2)
        print(res)
else:
    print(0)
    
    
