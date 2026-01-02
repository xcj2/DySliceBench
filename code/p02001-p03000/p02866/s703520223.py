from collections import Counter

def read():
    N = int(input().strip())
    D = list(map(int, input().strip().split()))
    return N, D

def argsort(x):
    pairs = [(i, x[i]) for i in range(len(x))]
    pairs.sort(key=lambda a: a[1])
    return [a[0] for a in pairs]


def solve(N, D, P=998244353):
    D = [-1] + D
    count = Counter(D)
    count_max = max(count.keys())

    if not(D[1] == 0 and count[0] == 1):
        return 0

    result = 1
    for i in range(1, count_max + 1):
        if count[i] == 0:
            return 0
        n_childs = count[i]
        n_parents = count[i-1]
        ptn = n_parents ** n_childs
        result *= ptn
        result %= P
    return result

if __name__ == '__main__':
    inputs = read()
    print("%d" % solve(*inputs))
