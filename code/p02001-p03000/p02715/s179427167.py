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

N,K=LI()

BUF=[0]*(K+1)
for i in reversed(range(1, K+1)):
    pat = POW(K//i, N)
    for j in range(2, K+1):
        if i*j <= K:
            pat -= BUF[i*j]
        else:
            break
    # print("pat:{} i:{}".format(pat, i))
    BUF[i] = pat

res = 0
for i, j in enumerate(BUF):
    res += (i*j) % DVSR
print(res%DVSR)
