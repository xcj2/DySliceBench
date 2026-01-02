def LI():return list(map(int,input().split()))
def yes():return print("Yes")
def no():return print("No")
from collections import deque, defaultdict, Counter
# from heapq import heappop, heappush
# import math
# from decimal import Decimal

# def divisors(x):
#     ret=[]
#     for i in range(1,int(x**.5)+1):
#         if x%i==0:
#             ret.append(i)
#             if x//i==i:continue
#             ret.append(x//i)
#     return sorted(ret)

# print(divisors(64),2**6)            

def prime_factor(n):
    ass = []
    for i in range(2,int(n**0.5)+1):
        while n % i==0:
            ass.append(i)
            n = n//i
    if n != 1:
        ass.append(n)
    return ass

n=int(input())
pf=prime_factor(n)
pf=Counter(pf)
# print(pf)

def cng(x):
    le=2*x
    ret=-1
    mi=int(le**0.5)
    for i in range(mi-1,mi+10000):
        # print((i+1)*(i+2),le,i*(i+1))
        if (i+1)*(i+2)>le>=i*(i+1):
            ret=i
            # print((i+1)*(i+2),le,i*(i+1))
            break
        
    return ret

mp=[]   
for i in range(2*10**5):
    mp.append(cng(i))
# print(-1 in mp)

ans=0
for i in pf.values():
    ans+=mp[i]
    
print(ans)


