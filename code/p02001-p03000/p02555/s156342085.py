import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

class Twelveways:
    def __init__(self,n,m=10**9+7):
        self.num = n
        self.mod = m
        self.f = self.factorials()
        self.g = self.inverse()

    def factorials(self):
        # 0~n!のリスト
        f = [1, 1]
        for i in range(2, self.num + 1):
            f.append(f[-1] * i % self.mod)
        return f

    def inverse(self):
        # 0~n!の逆元のリスト
        g = [1]
        for i in range(self.num):
            g.append(pow(self.f[i + 1], self.mod - 2, self.mod))
        return g

    def combination(self, n, k):
        # nCk mod mを求める
        nCk = self.f[n] * self.g[n - k] * self.g[k]
        nCk %= self.mod
        return nCk


s = readint()
mod = 10**9+7

a = Twelveways(s)

ans = 0
for i in range(1,s//3+1):
    ans += a.combination(s-3*i+i-1,i-1)

print(ans%mod)




