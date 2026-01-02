k = int(input()) - 1
def onesearch(last):
    if last < 0:
        return [9, 1]
    elif last == 0:
        return [2, 0]
    elif last == 9:
        return [2, 8]
    else:
        return [3, last - 1]
memo = {}
def search(i, last, rest):
    # print('search', (i, last, rest))
    if i == 0:
        n, base = onesearch(last)
        if rest < n:
            return (n, base + rest)
        else:
            return (n, -1)
    if (i, last) in memo:
        n, ret = memo[(i, last)]
        if ret >= 0:
            return (n, ret)
    n = 0
    if last < 0:
        for j in range(1, 10):
            n1, ret = search(i - 1, j, rest)
            if ret >= 0:
                return (n1, j * 10 ** i + ret)
            n += n1
            rest -= n1
        memo[(i, last)] = (n, -1)
        return (n, -1)
    for j in range(max(0, last - 1), min(10, last + 2)):
        n1, ret = search(i - 1, j, rest)
        if ret >= 0:
            return (n1, j * 10 ** i + ret)
        n += n1
        rest -= n1
    memo[(i, last)] = (n, -1)
    return (n, -1)
def sub(k):
    for i in range(20):
        n, ret = search(i, -1, k)
        if ret >= 0:
            return ret
        k -= n

print(sub(k))
