import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    N, M = map(int, readline().split())
    A = list(set(map(int, readline().split())))

    B = A[::]
    while not any(b % 2 for b in B):
        B = [b // 2 for b in B]

    if not all(b % 2 for b in B):
        print(0)
        return

    semi_lcm = 1
    for a in A:
        semi_lcm = lcm(semi_lcm, a // 2)
        if semi_lcm > M:
            print(0)
            return

    print((M // semi_lcm + 1) // 2)
    return


if __name__ == '__main__':
    main()
