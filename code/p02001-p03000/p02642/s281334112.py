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

    #[(p1,n1),(p2,n2),...]の形で返す
    def primeFactor2(n):
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

    #約数列挙
    #10^6以下で約数の数が最大なのは720720の時(240個しかない！)
    def divisors(N):
        pf = primeFactor(N)
        ret = [1]
        for p in pf:
            ret_prev = ret
            ret = []
            for i in range(pf[p]+1):
                for r in ret_prev:
                    ret.append(r * (p ** i))
        return sorted(ret)
        
        
    
    mod=10**9+7
    N=I()
    A=LI()
    from collections import defaultdict
    dd = defaultdict(int)
    for i in range(N):
        dd[A[i]]+=1
        
    A.sort()
    
    ans=0
    for i in range(N):
        if dd[A[i]]<2:
            L=divisors(A[i])
            flag=1
            for v in L[:-1]:
                if dd[v]:
                    flag=0
                    break
            if flag:
                ans+=1
                
    if A.count(1)==1:
        ans=1
    
                
    print(ans)
                    
        
        

                
    
    


main()
