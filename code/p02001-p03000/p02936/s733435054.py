import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
mod = 10**9+7
Max = sys.maxsize
def l(): #intのlist
    return list(map(int,input().split()))
def m(): #複数文字
    return map(int,input().split())
def onem(): #Nとかの取得
    return int(input())
def s(x): #圧縮
    a = []
    aa = x[0]
    su = 1
    for i in range(len(x)-1):
        if aa != x[i+1]:
            a.append([aa,su])
            aa = x[i+1]
            su = 1
        else:
            su += 1
    a.append([aa,su])
    return a
def jo(x): #listをスペースごとに分ける
    return " ".join(map(str,x))
def max2(x): #他のときもどうように作成可能
    return max(map(max,x))
import fractions
from functools import reduce
def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)
def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


n,q = m()

count = [0 for i in range(n)]

root = [[] for i in range(n)]

for i in range(n-1):
    a,b = m()
    a -= 1
    b -= 1
    root[a].append(b)

for i in range(q):
    a,b = m()
    a -= 1
    count[a] += b
de = cl.deque()

for i in range(len(root[0])):
    count[root[0][i]] += count[0]
    de.append(root[0][i])
while de:
    k = de.popleft()
    for i in range(len(root[k])):
        count[root[k][i]] += count[k]
        de.append(root[k][i])
print(jo(count))


