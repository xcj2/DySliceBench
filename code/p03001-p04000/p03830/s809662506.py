import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    N=int(input())
    import math
    def prime_factorize1(N):
        """
        Nをくって、Nの素因数を格納したリストresを返す。
        リストの要素をすべて掛ければNになる"""
        res = []
        x = N
        y = 2
        while y*y <= x:
            while x % y == 0:
                res.append(y)
                x //= y
            y += 1
        if x > 1:
            res.append(x)
        return res
    if N==1:
        print(1)
    else:
        num=[]
        for i in range(2,N+1):
            l=prime_factorize1(i)
            num.extend(l)
        from collections import Counter
        c=Counter(num)
        ans=1
        for x in c.values():
            ans=(ans*(x+1))%(10**9+7)
        print(ans)
resolve()