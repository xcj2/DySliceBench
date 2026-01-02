from sys import stdin, setrecursionlimit


def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


def lcm(x, y):
    return x * y // gcd(x, y)


def main():
    input = stdin.buffer.readline
    a, b, c, d = map(int, input().split())
    l = lcm(c, d)
    ans = 0
    ans += (l - (l // c + l // d - 1)) * (b // l - (a - 1)//l)
    tmp_b = b % l
    ans += tmp_b - (tmp_b // c + tmp_b // d)
    tmp_a = (a - 1) % l
    ans -= tmp_a - (tmp_a // c + tmp_a // d)
    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
