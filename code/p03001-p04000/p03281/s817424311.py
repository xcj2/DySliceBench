import sys
input = sys.stdin.readline


def readstr():
    return input().strip()


def readint():
    return int(input())


def readnums():
    return map(int, input().split())


def readstrs():
    return input().split()


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


N = readint()
ans = 0
for i in range(1, N + 1, 2):
    if len(make_divisors(i)) == 8:
        ans += 1

print(ans)
