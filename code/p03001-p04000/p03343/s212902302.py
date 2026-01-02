import heapq

def main():
    _, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    idx = make_index(a)
    groups = [(0, len(a))]

    m = float('inf')
    for y in sorted(set(a)):
        xs = []
        for start, stop in groups:
            xs.extend(nsmallest(min(stop - start - k + 1, q), a, start, stop))

        if len(xs) < q:
            break

        xxs = heapq.nsmallest(q, xs)
        x = xxs[-1]
        m = min(m, x - y)

        groups = split_groups(idx[y], groups, k)

    print(m)

MEMO = dict()
def nsmallest(n, a, start, stop):
    global MEMO
    key = (n, id(a), start, stop)
    if key in MEMO:
        return MEMO[key]

    val = heapq.nsmallest(n, a[start:stop])
    MEMO[key] = val
    return val

def split_groups(pivots, groups, k):
    gs = []

    i = 0
    for start, stop in groups:
        while i < len(pivots) and pivots[i] < start:
            i += 1
        while i < len(pivots) and pivots[i] <= stop:
            if pivots[i] - start >= k:
                gs.append((start, pivots[i]))
            start = pivots[i] + 1
            i += 1

        if stop - start >= k:
            gs.append((start, stop))

    return gs


def make_index(a):
    idx = dict()

    for i, x in enumerate(a):
        if x in idx:
            idx[x].append(i)
        else:
            idx[x] = [i]

    return idx

main()
