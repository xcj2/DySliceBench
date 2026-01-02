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

N=II()
inl = [LI() for i in range(N)]
inl.sort(key=lambda x: x[2], reverse=True)

st=set()
prevset=set()
for x,y,h in inl:
    st = set()
    for i in range(101):
        for j in range(101):
            abso = abs(x-i)+abs(y-j)
            if not h == 0:
                st.add((i,j, h+abso))
            else:
                for k in range(1, abso+1):
                    st.add((i,j, k))

    prevset = st if not prevset else st.intersection(prevset)
    if len(prevset) == 1:
        break

print(*prevset.pop())
