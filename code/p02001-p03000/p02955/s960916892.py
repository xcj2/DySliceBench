import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time
sys.setrecursionlimit(10**7)
inf = 10**20

N,K = map(int,input().split())
A = list(map(int,input().split()))

def distance(x,d):
    r = x%d
    return(min(r,d-r))

def cost(d,numList):
    r = list(map(lambda x: x%d, numList))
    r.sort(reverse=True)
    p = sum(r)//d
    c = 0
    for i in range(p):
        c += d - r[i]
    return(c)

def divisors(n):
    sq = math.ceil(math.sqrt(n))
    ans = []
    for i in range(1,sq):
        if n%i == 0:
            ans.append(i)
            ans.append(n//i)
    return(ans)

s = sum(A)
divs = divisors(s)
ans = 1
for d in divs:
    c = cost(d, A)
    if c <= K:
        ans = max(ans,d)
print(ans)