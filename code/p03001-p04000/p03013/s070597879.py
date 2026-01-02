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

N,M = LI()

st = set()
for i in range(M):
    st.add(int(input()))

pat1 = 1
pat2 = 0

for i in range(1, N):
    tmp = pat2
    pat2 = pat1
    pat1 = ((pat1 + tmp)%MOD) if not i in st else 0
    # print('pat1: {} pat2: {} i:{}'.format(pat1, pat2, i))
print((pat1+pat2)%MOD)
