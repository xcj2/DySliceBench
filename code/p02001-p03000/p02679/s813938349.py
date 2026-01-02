def Int():
    return int(input())
def Ints():
    return map(int,input().split())
def IntList():
    return list(Ints())
def IntMat(N):
    return [IntList() for i in range(N)]

import sys
sys.setrecursionlimit(4100000)
input = sys.stdin.readline

N = Int()
mod = 1000000007
ans = 1
import math

from collections import defaultdict
XX = defaultdict(list)
YY = defaultdict(list)

zeros = 0

for i in range(N):
    A,B = Ints()
    if A!=0 and B!=0:
        GCD = math.gcd(A,B)
        A //=GCD
        B //=GCD
        if A<0 and B<0:
            A *= -1
            B *= -1
        elif A>0 and B<0:
            A *= -1
            B *= -1
        XX[(A,B)].append(i)
        
        B *= -1
        if A<0 and B<0:
            A *= -1
            B *= -1
        elif A<0 and B>0:
            A *= -1
            B *= -1
        YY[(B,A)].append(i)
        
    elif A==0 and B!=0:
        XX[(0,1)].append(i)
        YY[(1,0)].append(i)
    elif A!=0 and B==0:
        XX[(1,0)].append(i)
        YY[(0,1)].append(i)
    else:
        zeros += 1


D = {}

for key in XX:
    if not key in D:
        l = len(XX[key])
        m = len(YY[key])
        ans *= (pow(2,l,mod)+pow(2,m,mod)-1)
        ans %= mod
        D[key] = 1
        
        a,b = key
        if a==0 and b==1:
            D[(1,0)] = 1
        elif a==1 and b==0:
            D[(0,1)] = 1
        else:
            b *= -1
            if a < 0:
                b*=-1
                a*=-1
            D[(b,a)] = 1
    
ans -= 1
ans += zeros
ans %= mod
print(ans)