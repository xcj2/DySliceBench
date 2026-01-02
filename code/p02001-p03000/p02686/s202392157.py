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

LSTP=[]
LSTN=[]
for i in range(N):
    cnt = 0
    cntMin = 0
    s = input()
    for c in s:
        if c == "(":
            cnt += 1
        else:
            cnt -= 1
        cntMin = min(cntMin, cnt)
    # print(cntMin)
    if cnt >= 0:
        LSTP.append((cntMin, cnt))
    else:
        LSTN.append((-(cnt-cntMin), -cnt))

LSTP.sort(reverse=True)
LSTN.sort(reverse=True)

res = 0
for cntMin, cnt in LSTP:
    if res + cntMin < 0:
        print("No")
        exit(0)
    res += cnt

res2 = 0
for cntMin, cnt in LSTN:
    if res2 + cntMin < 0:
        print("No")
        exit(0)
    res2 += cnt

if res - res2 == 0:
    print("Yes")
else:
    print("No")
