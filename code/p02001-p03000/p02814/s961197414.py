def main():
    from functools import reduce

    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)

    def lcm(a, b):
        return (a // gcd(a, b)) * b

    N, M = map(int, input().split())
    *a, = map(int, input().split())

    p = -1
    b = []
    for x in a:
        cnt = 0
        while x % 2 == 0:
            x //= 2
            cnt += 1
        if ~p and p != cnt:
            print(0)
            return
        p = cnt
        b.append(x)

    if p == 0:
        print(0)
        return

    t = pow(2, p - 1) * reduce(lcm, b)
    ans = (M // t) - (M // (t * 2))

    print(ans)


if __name__ == '__main__':
    main()

# import sys
#
# sys.setrecursionlimit(10 ** 7)
#
# input = sys.stdin.readline
# rstrip()
# int(input())
# map(int, input().split())
