import sys
from itertools import product as prd
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
MOD = 1000000007
def POW(x, y): return pow(x, y, MOD)
def INV(x, m=MOD): return pow(x, m - 2, m)
def DIV(x, y, m=MOD): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

S = input()
X,Y=LI()

while S and S[0] == 'F':
    S = S[1:]
    X -= 1
isX = True
cur = 0
xs = []
ys = []
for i in range(len(S)):
    if S[i] == 'T':
        if cur:
            if isX: xs.append(cur)
            else: ys.append(cur)
        isX = not isX
        cur = 0
    elif S[i] == 'F': cur += 1

if cur:
    if isX: xs.append(cur)
    else: ys.append(cur)
sumxs = sum(xs)
sumys = sum(ys)

if abs(X) > sumxs or abs(Y) > sumys:
    print('No')
    exit()

memo1 = [[0]*(sumxs*2+1) for i in range(len(xs)+1)]
memo2 = [[0]*(sumys*2+1) for i in range(len(ys)+1)]

memo1[0][0] = 1
memo2[0][0] = 1
for i, j in prd(range(1, len(xs)+1), range(-sumxs, sumxs+1)):
    memo1[i][j] = memo1[i-1][j+xs[i-1]] or memo1[i-1][j-xs[i-1]]

for i, j in prd(range(1, len(ys)+1), range(-sumys, sumys+1)):
    memo2[i][j] = memo2[i-1][j+ys[i-1]] or memo2[i-1][j-ys[i-1]]

print('Yes' if memo1[len(xs)][X] and memo2[len(ys)][Y] else 'No')
