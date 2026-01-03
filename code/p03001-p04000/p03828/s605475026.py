from collections import defaultdict

def read_input():
    n = int(input())

    return n


def factorizer(x):
    limit = x

    factors = []
    t = x
    for i in range(2, limit + 1):
        while t % i == 0:
            factors.append(i)
            t /= i

    if not factors:
        factors.append(x)

    return factors


def submit():
    n = read_input()

    factors_occur = defaultdict(int)

    for i in range(2, n + 1):
        factors = factorizer(i)

        for f in factors:
            factors_occur[f] += 1

    occurs = [o for (k, o) in factors_occur.items()]

    acc = 1
    maxmod = (10**9) + 7
    for power in occurs:
        acc *= (power + 1)

    print(acc % maxmod)

if __name__ == '__main__':
    submit()
