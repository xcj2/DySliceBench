import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def main():
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def soin(x):
        res = []
        cnt = 0
        while x % 2 == 0:
            x //= 2
            cnt += 1
        if cnt: res.append(cnt)
        d = 3
        while d ** 2 <= x:
            cnt = 0
            while x % d == 0:
                x //= d
                cnt += 1
            if cnt: res.append(cnt)
            d += 2
        if x != 1: res.append(1)
        return res

    a, b = map(int, input().split())
    g = gcd(a, b)
    e = soin(g)
    print(len(e) + 1)

main()
