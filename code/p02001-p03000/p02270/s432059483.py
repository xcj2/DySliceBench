import sys


def allocate(count, weights):
    """allocate all packages of weights onto trucks.
    returns maximum load of trucks.

    >>> allocate(2, [1, 2, 2, 6])
    6
    >>> allocate(3, [8, 1, 7, 3, 9])
    10
    """
    def loadable_counts(maxweight):
        n = 0
        l = 0
        c = count
        for w in weights:
            l += w
            if l > maxweight:
                l = w
                c -= 1

            if c <= 0:
                return n

            n += 1
        return n

    i = max(weights)
    j = max(weights) * len(weights) // count

    while i < j:
        mid = (i + j) // 2
        if loadable_counts(mid) < len(weights):
            i = mid + 1
        else:
            j = mid

    return i


def run():
    k, n = [int(i) for i in input().split()]
    ws = []
    for i in sys.stdin:
        ws.append(int(i))

    print(allocate(n, ws))


if __name__ == '__main__':
    run()

