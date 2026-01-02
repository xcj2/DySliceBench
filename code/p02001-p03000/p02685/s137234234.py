#!/usr/bin/env python3
import sys

MOD = 998244353  # type: int


class ModOperator:
    def __init__(self, MOD: int = 10 ** 9 + 7):
        self.MOD = MOD
        self.factorials = [1, 1]

    # x^n % MOD
    def mod_pow(self, x: int, n: int):
        bi = str(format(n, "b"))
        res = 1
        a = x
        for i in range(len(bi)):
            if n >> i & 1:
                res = (res * a) % self.MOD
            a = (a * a) % self.MOD
        return res
    
    # x! % MOD
    def mod_fact(self, x: int):
        if x < len(self.factorials):
            return self.factorials[x]
        else:
            res = self.factorials[-1]
            for i in range(len(self.factorials), x + 1):
                res = res * i % self.MOD
                self.factorials.append(res)
        return res % self.MOD

    # inverse of a number
    def mod_inv(self, x: int):
        return self.mod_pow(x, self.MOD - 2)
    
    # conmination nCk
    def mod_comb(self, n: int, k: int):
        numerator = self.mod_fact(n)
        denomintator1 = self.mod_fact(k)
        denomintator2 = self.mod_fact(n - k)
        denomintator = denomintator1 * denomintator2 % self.MOD
        return numerator * self.mod_inv(denomintator) % self.MOD

def main():
    N, M, K = map(int, input().split())

    op = ModOperator(MOD)
    sum = 0
    for i in range(K + 1):
        sum += M * op.mod_pow(M - 1, N - 1 - i) * op.mod_comb(N - 1, i)
    print(sum % MOD)


if __name__ == '__main__':
    main()
