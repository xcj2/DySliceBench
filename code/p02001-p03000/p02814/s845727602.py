import sys
from functools import reduce
sys.setrecursionlimit(10**6)


def main():

    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)

    def lcm_base(x, y):
        return (x * y) // gcd(x, y)

    def lcm(*numbers):
        return reduce(lcm_base, numbers, 1)

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    a0 = a[0]
    p = 0
    while a0 % 2 == 0:
        a0 //= 2
        p += 1
    elm = 2**p

    for ai in a:
        if (ai/elm) % 2 != 1:
            print(0)
            return

    lcm = lcm(*a)
    ans = (2*m+lcm) // (lcm*2)
    print(ans)


if __name__ == '__main__':
    main()
