import sys
input = sys.stdin.readline
sys.setrecursionlimit(2 * 10**6)


def inpl():
    return list(map(int, input().split()))


def f(x, y, z):
    return x**2 + y**2 + z**2 + x * y + y * z + z * x


def count(x, y, z):
    if x == y == z:
        return 1
    elif x == y or y == z:
        return 3
    else:
        return 6


def solve(n):
    x = 1
    ans = 0
    Z_MAX = int(n**0.5) + 1
    while f(x, x, x) <= n:
        y = x
        while f(x, y, y) <= n:
            z_min = y
            z_max = Z_MAX
            while z_max - z_min > 1:
                # print(z_max, z_min)
                t = (z_max + z_min) // 2
                if f(x, y, t) < n:
                    z_min = t + 1
                elif f(x, y, t) > n:
                    z_max = t
                else:
                    z_min = t
            if f(x, y, z_min) == n:
                ans += count(x, y, z_min)

            y += 1
        x += 1

    return ans


def main():
    N = int(input())
    for i in range(1, N + 1):
        print(solve(i))

    return


if __name__ == '__main__':
    main()
