import sys
sys.setrecursionlimit(10**5)

def L(): return [x for x in input().split()]
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LI_(): return [-1*int(x) for x in input().split()]
def II(): return int(input())
def IF(): return float(input())
def LM(func,n): return [[func(x) for x in input().split()]for i in range(n)]
mod = 1000000007
inf = float('INF')
dic = {"m":1000,"c":100,"x":10,"i":1}

def MCXI(S):
    ret = 0
    for d in "mcxi":
        i =S.find(d)
        if i >=1 and "2"<=S[i-1]<="9":
            ret  += int(S[i-1])*dic[d]
        elif i>=0:
            ret += dic[d]
    return ret
def mcxi(n):
    S = ""
    for d in "ixcm":
        if n%10 == 1:
            S += d
        elif n%10 > 1:
            S += d
            S += str(n%10)
        n //= 10
    return S[::-1]


n = II()

for i in range(n):
    a,b = L()
    a = MCXI(a)
    b= MCXI(b)
    print(mcxi(a+b))
