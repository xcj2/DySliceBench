# coding:utf-8

import sys

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n = II()
    train = [LI() for _ in range(n - 1)]

    for i in range(n):
        res = 0
        for c, s, f in train[i:]:
            if res <= s:
                res = c + s
            else:
                res += (f - (res - s) % f) % f + c

        print(res)


if __name__ == '__main__':
    main()
