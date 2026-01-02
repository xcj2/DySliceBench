#!/usr/bin/env python3
import sys
MOD = 1000000007  # type: int

# 逆元comb
def comb(n, k):
    k = min(n-k,k)
    ans = 1
    for i in range(1, k + 1):
        ans *= (n + 1 - i) * pow(i,MOD-2,MOD)
        ans %= MOD
    return ans

def solve(X: int, Y: int):
    if (X+Y)%3 != 0 or Y*2-X < 0 or X*2-Y < 0:
        print(0)
        return

    # (1,2)の移動をa回, (2,1)の移動をb回するとするをそれぞれ何回か決まる
    a = (Y*2-X)//3
    b = (X*2-Y)//3
    print(comb(a+b,a))
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(X, Y)

if __name__ == '__main__':
    main()
