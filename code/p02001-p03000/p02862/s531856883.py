from collections import defaultdict

# nCkを高速に求める
# https://drken1215.hatenablog.com/entry/2018/06/08/210000


class COM:
    def __init__(self, n, MOD):
        self.n = n
        self.MOD = MOD
        self.fac = [0] * (n+1)
        self.finv = [0] * (n+1)
        self.inv = [0] * (n+1)
        self.fac[0] = self.fac[1] = 1
        self.finv[0] = self.finv[1] = 1
        self.inv[1] = 1
        for i in range(2, n+1):
            self.fac[i] = self.fac[i-1] * i % MOD
            self.inv[i] = MOD - self.inv[MOD % i] * (MOD // i) % MOD
            self.finv[i] = self.finv[i-1] * self.inv[i] % MOD

    
    def calc(self, k):
        if k < 0:
            return 0
        return self.fac[self.n] * (self.finv[k] * self.finv[self.n-k] % self.MOD) % self.MOD


def main():
    MOD = 10**9+7
    X, Y = map(int,input().split())
    if (X+Y) % 3 == 0:
        z = (X+Y) // 3
        a_x = X-z
        a_y = Y-z
        if a_x >= 0 and a_y >= 0:
            com = COM(a_x+a_y, MOD)
            print(com.calc(a_x))
        else:
            print(0)
    else:
        print(0)

if __name__ == "__main__":
    main()



