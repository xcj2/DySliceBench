from collections import Counter
from itertools import combinations


def prime_factors(n):
    c = Counter()
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                c.update([i])
                n //= i
                break
    return c


def factrials(n):
    c = {}
    for i in range(2, n + 1):
        d = prime_factors(i)
        for k, v in d.items():
            if k in c:
                c[k] += v
            else:
                c[k] = v
    return c


def solve(N):
    facts = factrials(N)
    over2 = [k for k, v in facts.items() if v >= 2]
    over4 = [k for k, v in facts.items() if v >= 4]
    over14 = [k for k, v in facts.items() if v >= 14]
    over24 = [k for k, v in facts.items() if v >= 24]
    over74 = [k for k, v in facts.items() if v >= 74]

    sum = 0
    # 4 - 4 - 2
    sum += len([(d, d4) for d in over2 for d4 in combinations(over4, 2) if d not in d4])
    # 4 - 14
    sum += len([(d, d4) for d in over14 for d4 in over4 if d != d4])
    # 2 - 24
    sum += len([(d, d2) for d in over24 for d2 in over2 if d != d2])
    # 74
    sum += len(over74)

    return sum

if __name__ == "__main__":
    print(solve(int(input())))
