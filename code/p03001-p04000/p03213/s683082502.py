def main():
    from collections import Counter

    N = int(input())

    p = [0] * (N + 1)
    for x in range(2, N + 1):
        d = 2
        cnt = 0
        while x % d == 0:
            x //= d
            cnt += 1
        p[d] += cnt

        d = 3
        while x > 1:
            cnt = 0
            while x % d == 0:
                x //= d
                cnt += 1
            p[d] += cnt
            d += 2

    ctr = Counter(p)

    def count(n):
        ret = 0
        for pw, cnt in ctr.items():
            if pw >= n - 1:
                ret += cnt
        return ret

    def choose(n, r):
        x, y = 1, 1
        for i in range(r):
            x *= n - i
            y *= i + 1
        return x // y

    ans = count(75)
    ans += count(25) * (count(3) - 1)
    ans += count(15) * (count(5) - 1)
    ans += choose(count(5), 2) * (count(3) - 2)

    print(ans)


if __name__ == '__main__':
    main()

# import sys
# input = sys.stdin.readline
# 
# sys.setrecursionlimit(10 ** 7)
# 
# (int(x)-1 for x in input().split())
# rstrip()
#
# def binary_search(*, ok, ng, func):
#     while abs(ok - ng) > 1:
#         mid = (ok + ng) // 2
#         if func(mid):
#             ok = mid
#         else:
#             ng = mid
#     return ok
