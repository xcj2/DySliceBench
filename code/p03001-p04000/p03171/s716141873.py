import sys
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, d=DVSR): return pow(x, d - 2, d)
def DIV(x, y, d=DVSR): return (x * INV(y, d)) % d
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())

N=II()
A=LI()
MEMO = [[0]*(N+1) for i in range(N+1)]
turn = -1 if N%2 == 0 else 1
for i in range(N): MEMO[i][i+1] = turn*A[i] 

for wid in range(2, N+1):
    turn *= -1
    for i in range(N-wid+1):
        xy1 = MEMO[i+1][i+wid] + turn*A[i]
        xy2 = MEMO[i][i+wid-1] + turn*A[i+wid-1]
        MEMO[i][i+wid] = xy1 if turn*xy1 > turn*xy2 else xy2

print(MEMO[0][N])
