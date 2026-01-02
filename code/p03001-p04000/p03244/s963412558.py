import sys
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
def II(): return int(input())

L=II()
INL=LI()

ODDS=INL[::2]
EVNS=INL[1::2]

MP_ODDS = {}
MP_EVNS = {}

if L == 2:
    print(0)
    exit()

for i in ODDS:
    if not i in MP_ODDS:
        MP_ODDS[i] = 0
    MP_ODDS[i] += 1

for i in EVNS:
    if not i in MP_EVNS:
        MP_EVNS[i] = 0
    MP_EVNS[i] += 1

ODDSC = []
EVNSC = []
for i,j in MP_ODDS.items():
    ODDSC.append((j,i))
for i,j in MP_EVNS.items():
    EVNSC.append((j,i))
ODDSC.sort(reverse=True)
EVNSC.sort(reverse=True)
EVNSC.append((0, -1))
ODDSC.append((0, -1))

# print(ODDSC, L)
if ODDSC[0][1] == EVNSC[0][1]:
    print(min(L-ODDSC[1][0]-EVNSC[0][0], L-ODDSC[0][0]-EVNSC[1][0]))    
else:
    print(L - ODDSC[0][0] - EVNSC[0][0])
