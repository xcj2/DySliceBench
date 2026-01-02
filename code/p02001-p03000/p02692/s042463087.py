import sys
from math import log2,floor,ceil,sqrt
# import bisect
# from collections import deque

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

n,a,b,c = Ri()
ans  = []
flag = True
q = []
for i in range(n):
    temp = ri()
    q.append(temp)

ac = [INF]*n
ab = [INF]*n
bc = [INF]*n
nac = INF
nab = INF
nbc = INF
for i in range(n-1,-1,-1):
    ac[i] = nac
    ab[i] = nab
    bc[i] = nbc
    if q[i] == 'AC':
        nac = i
    elif q[i] == 'AB':
        nab = i
    else:
        nbc = i

for i in range(n):
    # temp = ri()
    temp = q[i]
    if temp == "AB":
        if a==0 and b==0:
            flag = False
        else:
            if a<b:
                # if a== 0 and b==1:

                a+=1
                b-=1
                ans.append("A")
            else:
                if a==1 and b==1 and c==0:
                    if ac[i] < bc[i]:
                        a+=1
                        b-=1
                        ans.append('A')
                    else:
                        b+=1
                        a-=1
                        ans.append('B')
                else:
                    a-=1
                    b+=1
                    ans.append("B")
    elif temp == "BC":
        # print(a,b,c)
        if c==0 and b==0:
            flag = False
        else:
            if c<b:
                # print("faf")
                c+=1
                b-=1
                ans.append("C")
                # print(ans)
            else:
                if c==1 and b==1 and a==0:
                    if ac[i] < ab[i]:
                        c+=1
                        b-=1
                        ans.append('C')
                    else:
                        b+=1
                        c-=1
                        ans.append('B')
                else:
                    c-=1
                    b+=1
                    ans.append("B")
    else:
        if a==0 and c==0:
            flag = False
        else:
            if a<c:
                a+=1
                c-=1
                ans.append("A")
            else:
                if a==1 and c==1 and b==0:
                    if ab[i] < bc[i]:
                        a+=1
                        c-=1
                        ans.append('A')
                    else:
                        c+=1
                        a-=1
                        ans.append('C')
                else:
                    a-=1
                    c+=1
                    ans.append("C")
if not flag : 
    No()
else:
    Yes()
    for i in range(n):
        print(ans[i])
        
