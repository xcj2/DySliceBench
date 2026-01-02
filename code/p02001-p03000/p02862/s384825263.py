import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    def main():
        X,Y=map(int,input().split())
        n=(-X+2*Y)/3
        m=(2*X-Y)/3

        # https://atcoder.jp/contests/abc156/submissions/11621672
        def modpow(a, b, mod=10 ** 9 + 7):
            ret = 1
            while b > 0:
                if b % 2 == 1:
                    ret = ret * a % mod
                a = a * a % mod
                b //= 2
            return ret
        
        
        def modcomb(n, c, mod=10 ** 9 + 7):
            if c > n - c:
                c = n - c
            u, d = 1, 1
            for i in range(c):
                u = u * (n - i) % mod
                d = d * (i + 1) % mod
            return u * modpow(d, mod - 2) % mod
        
        
        """mod = 10 ** 9 + 7
        n, a, b = map(int, input().split())
        ans = (modpow(2, n) - 1) % mod
        ans = (ans-modcomb(n, a)) % mod
        ans = (ans-modcomb(n, b)) % mod
        print(ans)"""
        
        # combどうしの積をとると余りがずれるので避ける！　普通のcombを計算して最後にmodをとって。
        
        # comb(n + k - 1, n) # 重複組み合わせkHn．k種類の箱にn個の玉        
        if n.is_integer() and m.is_integer() and n>=0 and m>=0:
            return modcomb(int(n+m),int(n))
        else: return 0
    print(main())
    
resolve()