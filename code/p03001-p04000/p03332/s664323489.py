# RGB coloring


import math
mod = 998244353


class Combi():
    def __init__(self, N, mod):
        self.power = [1 for _ in range(N+1)]
        self.rev = [1 for _ in range(N+1)]
        self.mod = mod
        for i in range(2, N+1):
            self.power[i] = (self.power[i-1]*i) % self.mod
        self.rev[N] = pow(self.power[N], self.mod-2, self.mod)
        for j in range(N, 0, -1):
            self.rev[j-1] = (self.rev[j]*j) % self.mod

    def C(self, K, R):
        if K < R:
            return 0
        else:
            return ((self.power[K])*(self.rev[K-R])*(self.rev[R])) % self.mod

    def P(self, K, R):
        if K < R:
            return 0
        else:
            return (self.power[K])*(self.rev[K-R]) % self.mod


def main():
    N, A, B, K = map(int, input().split())
    c = Combi(N, mod)    
    res = 0
    for i in range(N+1):
        if (K-A*i) % B == 0 and K >= A*i:
            res += c.C(N, i)*c.C(N, (K-A*i)//B)
    res %= mod
    print(res)


if __name__ == "__main__":
    main()