from collections import defaultdict


def f(edges, start):
    mp = defaultdict(lambda: [])
    for a, b in edges:
        mp[a].append(b)
        mp[b].append(a)

    res = {start}
    q = [start]

    while True:
        if len(q) == 0:
            return res
        i = q.pop()
        nei = mp[i]
        for j in nei:
            if j in res:
                continue
            res.add(j)
            q.append(j)
    return res


def check(n, edges, start):
    a = f(edges, start)
    return len(a) != n


def main():
    n, m = [int(a) for a in input().split()]
    ab = [
        [int(a) - 1 for a in input().split()]
        for _ in range(m)
    ]

    c = 0
    for i in range(m):
        if check(n, ab[:i] + ab[i + 1:], ab[i][0]):
            c += 1
    print(c)


if __name__ == '__main__':
    main()
