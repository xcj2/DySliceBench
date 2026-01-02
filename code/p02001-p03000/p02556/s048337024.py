def sep():
    return map(int,input().strip().split(" "))
import sys
sys.setrecursionlimit(2*10**5)
from random import randint
def lis():
    return list(sep())

def maxAbsValExpr(x, y):
    res, n = 0, len(y)
    for p, q in [ [-1, 1], [-1, -1],[1, 1], [1, -1]]:
        smallest = p * x[0] + q * y[0] + 0
        for i in range(n):
            cur =   q * y[i] + p * x[i]
            res = max(res, cur - smallest)
            smallest = min(smallest, cur)
    return res
n=int(input())
x=[]
y=[]
for _ in range(n):
    a,b=sep()
    x.append(a)
    y.append(b)
print(maxAbsValExpr(x,y))

