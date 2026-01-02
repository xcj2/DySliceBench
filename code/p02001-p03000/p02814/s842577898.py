def main():
    import sys
    input = sys.stdin.buffer.readline

    def gcd(x, y):
        if y == 0:
            return x
        while y != 0:
            x, y = y, x % y
        return x

    def lcm(x, y):
        return x*y//gcd(x, y)

    N, M = (int(i) for i in input().split())
    A = [int(i)//2 for i in input().split()]
    cnt = [0]*(N)
    for i, a in enumerate(A):
        while a % 2 == 0:
            cnt[i] += 1
            a //= 2
    if any(cnt[0] != c for c in cnt):
        return print(0)
    L = 1
    for a in A:
        L = lcm(L, a)

    ans = 0
    mul = 1
    while L*mul <= M:
        ans += 1
        mul += 2
    print(ans)


if __name__ == '__main__':
    main()
