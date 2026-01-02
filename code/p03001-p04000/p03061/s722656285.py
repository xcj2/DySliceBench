from functools import lru_cache
from sys import stdin


@lru_cache(maxsize=None)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def make_acc_gdbs(As):
    result = []
    tmp = 0
    for x in As:
        tmp = gcd(tmp, x)
        result.append(tmp)
    return result


def main():
    N = int(stdin.readline().rstrip())
    As = [int(x) for x in stdin.readline().rstrip().split()]
    lAs = make_acc_gdbs(As)
    rAs = make_acc_gdbs(As[::-1])[::-1]
    max_ = 0
    for i in range(N):
        left = 0 if i == 0 else lAs[i - 1]
        right = 0 if i == (N - 1) else rAs[i + 1]
        max_ = max(max_, gcd(left, right))
    print(max_)


if __name__ == "__main__":
    main()
