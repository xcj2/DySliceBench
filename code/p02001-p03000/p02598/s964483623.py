import math

LI = lambda: list(map(int, input().split()))

N, K = LI()
A = LI()


def judge(x):
    k = 0
    for a in A:
        if a <= x:
            continue
        if a % x == 0:
            k += a // x - 1
        else:
            k += a // x
    if k <= K:
        return True
    else:
        return False


def solve():
    left, right = 0, max(A)
    while right - left > 1:
        x = (left + right) // 2
        if judge(x):
            right = x
        else:
            left = x
    return right


def main():
    ans = solve()
    print(ans)


if __name__ == "__main__":
    main()
