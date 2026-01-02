import sys
from collections import deque
import itertools


def input():
    return sys.stdin.readline().rstrip()


def main():
    x,y = map(int,input().split())
    if (x+y)%3 !=0:
        print(0)
        exit()
    if x*2 <y or y *2 <x:
        print(0)
        exit()

    n = int((x+y)/3)
    #conbination y-n from N or  x-n from N


    mod = 10 ** 9 + 7  # 出力の制限
    N = 10 ** 6
    g1 = [1, 1]  # 元テーブル
    g2 = [1, 1]  # 逆元テーブル
    inverse = [0, 1]  # 逆元テーブル計算用テーブル

    def cmb(n, r, mod):
        if (r < 0 or r > n):
            return 0
        r = min(r, n - r)
        return g1[n] * g2[r] * g2[n - r] % mod
    for i in range(2, N + 1):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod // i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)

    a = cmb(n, x-n, mod)

    print(a)
if __name__ == "__main__":
    main()
