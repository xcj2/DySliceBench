import math
import fractions
from functools import reduce


def main():
    n = int(input())
    a = input_list()
    if len(set(a)) == 1:
        print(n//2)
        exit(0)
    evens = {}
    odds = {}
    for i, v in enumerate(a):
        if i % 2 == 0:
            if v in evens:
                evens[v] += 1
            else:
                evens[v] = 1
        else:
            if v in odds:
                odds[v] += 1
            else:
                odds[v] = 1
    if len(evens) == 1 and len(odds) == 1:
        print(0)
        exit(0)

    e = sorted(evens.items(), key=lambda x: x[1], reverse=True)
    o = sorted(odds.items(), key=lambda x: x[1], reverse=True)
    if e[0][0] != o[0][0]:
        even_ans = (n // 2) - e[0][1]
        odd_ans = (n // 2) if len(o) == 1 else (n // 2) - o[0][1]
        a1 = even_ans+odd_ans

        even_ans = (n // 2) if len(e) == 1 else (n // 2) - e[0][1]
        odd_ans = (n // 2) - o[0][1]
        a2 = even_ans+odd_ans
        print(min(a1, a2))
    else:
        even_ans = (n // 2) - e[0][1]
        odd_ans = (n // 2) if len(o) == 1 else (n // 2) - o[1][1]
        a1 = even_ans + odd_ans

        even_ans = (n // 2) if len(e) == 1 else (n // 2) - e[1][1]
        odd_ans = (n // 2) - o[0][1]
        a2 = even_ans + odd_ans
        print(min(a1, a2))

# 6
# 3 1 3 2 4 2

def input_list():
    return list(map(int, input().split()))

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

if __name__ == "__main__":
    main()
