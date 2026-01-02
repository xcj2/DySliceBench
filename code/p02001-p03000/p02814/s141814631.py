from functools import reduce

def gcd(x,y):
    while y: x,y = y,x%y
    return x

def lcm(x,y):
    return x//gcd(x,y)*y

def ex_euclid(x,y):
    c0,c1 = x,y
    a0,a1 = 1,0
    b0,b1 = 0,1
    while c1:
        a0,a1 = a1,a0-c0//c1*a1
        b0,b1 = b1,b0-c0//c1*b1
        c0,c1 = c1,c0%c1
    return c0,a0,b0

N,M = map(int,input().split())
A = list(map(int,input().split()))

if N == 1:
    a = A[0]
    print((M-a//2%a)//a+1)

else:
    LCM = reduce(lcm,A)

    SCMs = []
    flag = True

    for i in range(N-1):
        c,a,b = ex_euclid(A[i],-A[i+1])
        if (A[i+1]-A[i])//2%c == 0:
            SCMs.append(A[i]*((A[i+1]-A[i])//2//c)*a+A[i]//2)
        else:
            flag = False
            break

    print((M-reduce(lcm,SCMs)%LCM)//LCM+1 if flag else 0)