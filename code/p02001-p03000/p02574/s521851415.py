import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    def gcd(a, b):
        while b: a, b = b, a % b
        return a
    def isPrimeMR(n):
        d = n - 1
        d = d // (d & -d)
        L = [2]
        for a in L:
            t = d
            y = pow(a, t, n)
            if y == 1: continue
            while y != n - 1:
                y = (y * y) % n
                if y == 1 or t == n - 1: return 0
                t <<= 1
        return 1
    def findFactorRho(n):
        m = 1 << n.bit_length() // 8
        for c in range(1, 99):
            f = lambda x: (x * x + c) % n
            y, r, q, g = 2, 1, 1, 1
            while g == 1:
                x = y
                for i in range(r):
                    y = f(y)
                k = 0
                while k < r and g == 1:
                    ys = y
                    for i in range(min(m, r - k)):
                        y = f(y)
                        q = q * abs(x - y) % n
                    g = gcd(q, n)
                    k += m
                r <<= 1
            if g == n:
                g = 1
                while g == 1:
                    ys = f(ys)
                    g = gcd(abs(x - ys), n)
            if g < n:
                if isPrimeMR(g): return g
                elif isPrimeMR(n // g): return n // g
                return findFactorRho(g)
    #[(p1,n1),(p2,n2),...]の形で返す
    def primeFactor(n):
        i = 2
        ret = {}
        rhoFlg = 0
        while i*i <= n:
            k = 0
            while n % i == 0:
                n //= i
                k += 1
            if k: ret[i] = k
            i += 1 + i % 2
            if i == 101 and n >= 2 ** 20:
                while n > 1:
                    if isPrimeMR(n):
                        ret[n], n = 1, 1
                    else:
                        rhoFlg = 1
                        j = findFactorRho(n)
                        k = 0
                        while n % j == 0:
                            n //= j
                            k += 1
                        ret[j] = k

        if n > 1: ret[n] = 1
        if rhoFlg: ret = {x: ret[x] for x in sorted(ret)}
        return ret
    
    from math import gcd
    N=I()
    A=LI()
    from collections import defaultdict
    dd = defaultdict(int)
    flag=1
    
    for i in range(N):
        a=A[i]
        ret=primeFactor(a)
        for p,pn in ret.items():
            if dd[p]:
                flag=0
                break
            dd[p]+=1
            
    if flag:
        print("pairwise coprime")
    else:
        g=A[0]
        for i in range(1,N):
            g=gcd(g,A[i])
        if g==1:
            print("setwise coprime")
        else:
            print("not coprime")
                
            
    

main()
