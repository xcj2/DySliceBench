
from functools import lru_cache
import math


@lru_cache(maxsize=None)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a*b//gcd(a, b)


def lcm_all(lst):
    curr = 1
    for l in lst:
        curr = lcm(curr, l)
    return curr


def divide_count(x):
    ans = 0
    while True:
        q, r = divmod(x, 2)
        if r == 0:
            ans += 1
            x = q
        else:
            break
    return ans



def submit():
    n, m = map(int, input().split())
    alist = list(map(int, input().split()))

    a_divide_count = [divide_count(a) for a in alist]
    for a in a_divide_count[1:]:
        if a != a_divide_count[0]:
            print(0)
            return

    l = lcm_all(alist)
    x = l // 2
    if x > m:
        print(0)
    else:
        print(math.ceil(m // x / 2))


if __name__ == "__main__":
    submit()