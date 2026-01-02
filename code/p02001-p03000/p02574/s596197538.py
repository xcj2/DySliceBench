#ソートなし版
import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def gcdlist(l):
    a = l[0]
    for i in range(1,len(l)):
        a = gcd(a,l[i])
    return a

def fctr1(n): 
    f = []
    c = 0
    for i in range(2,int(n**0.5)+2):
        while n%i == 0:
            c += 1
            n = n//i
        if c !=0:
            f.append([i,c])
            c = 0
    if n != 1:
        f.append([n,1])
    return f

n = int(readline())
a = list(map(int,readline().split()))
check = [True]*(10**6+5)
p1 = True
for ai in a:
    if not p1:
        break
    dlist = fctr1(ai)
    for d,c in dlist:
        if check[d]:
            check[d] = False
        else:
            p1 = False
            break

if p1:
    print("pairwise coprime")
else:
    p2 = gcdlist(a)
    if p2 == 1:
        print("setwise coprime")
    else:
        print("not coprime")


