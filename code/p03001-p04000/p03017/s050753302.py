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
def SI(): return input()

N,A,B,C,D=LI()
st=input()

if C < D:
    if st[A:C].find('##') >= 0 or st[B:D].find('##') >= 0:
        print('No')
    else:
        print('Yes')
else:
    # Cの方がおおきいケース 入れ替わる
    if st.find('##', A-1, C) >= 0:
        print('No')
    else:
        fnd = st.find('...', B-2, D+1)
        if fnd >= 0:
            print('Yes')
        else:
            print('No')
