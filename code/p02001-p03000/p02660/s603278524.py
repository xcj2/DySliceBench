import sys
from math import log2,floor,ceil,sqrt
# import bisect
# from collections import deque

# from types import GeneratorType
# def bootstrap(func, stack=[]):
#     def wrapped_function(*args, **kwargs):
#         if stack:
#             return func(*args, **kwargs)
#         else:
#             call = func(*args, **kwargs)
#             while True:
#                 if type(call) is GeneratorType:
#                     stack.append(call)
#                     call = next(call)
#                 else:
#                     stack.pop()
#                     if not stack:
#                         break
#                     call = stack[-1].send(call)
#             return call
#     return wrapped_function

Ri = lambda : [int(x) for x in sys.stdin.readline().split()]
ri = lambda : sys.stdin.readline().strip()
 
def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
INF = 10 ** 18
MOD = 10**9+7
N = 10**6 +1


# def seive():
#     for i in range(2*2,N+1,2):
#         prime[i] = False
#     # for j in range(divceil(l,2)*2 ,r+1,2):
#     #         divisor[j-l].append(2)
    
#     p= 3
#     while(p*p <= N):
#         if prime[p]:
#             for i in range(p*p,N+1,p):
#                 prime[i]  = False
#             # for j in range(divceil(l,p)*p ,r+1,p):
#             #     # if j == 18:
#             #     #     print("fs")
#             #     divisor[j-l].append(p)
#         p+=2

def solve(cnt):
    val = (-1+sqrt(1+8*cnt))/2
    return floor(val)


# prime = [True]*(N+1)
n = int(ri())

ans = 0
if n == 1:
    print(0)
else:
    p = 2
    while p*p <= n:
        cnt = 0
        while(n%p == 0):
            cnt+=1
            n= n//p
        if cnt != 0:
            # print(p)
            ans+=solve(cnt)
        p+=1
    if n != 1:
        ans +=1

    print(ans)

