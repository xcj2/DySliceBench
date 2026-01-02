from itertools import permutations


def resolve():
    n, m, x = map(int, input().split())
    inf = float('INF')
    data = [list(map(int, input().split())) for i in range(n)]

    if n > 6:
        d = get(data[:n//2], n//2, m)
        e = get(data[n//2:], n - n//2, m)
        d = merge(d,e,m)
    else:
        d = get(data, n, m)

    ans = inf
    for tt,cost in d.items():
        for t in tt:
            if x > t:
                break
        else:
            if ans > cost:
                ans = cost

    print(ans if ans != inf else -1)

def get(data, n, m):
    d = {}
    for b in range(1 << n):
        tmp = [0 for i in range(m)]
        cost = 0
        for i in range(n):
            if ((1<<i) & b) == 0:
                continue
            cost += data[i][0]
            for j in range(1,m+1):
                tmp[j-1] += data[i][j]
        tt = tuple(tmp)
        if tt not in d:
            d[tt] = cost
        else:
            if cost < d[tt]:
                d[tt] = cost
    return d

def merge(d,e,m):
    f = {}
    for k,v in d.items():
        for s,t in e.items():
            tt = tuple(k[i]+s[i] for i in range(m))
            cost = v + t
            if tt not in f:
                f[tt] = cost
            else:
                if cost < f[tt]:
                    f[tt] = cost
    return f

if __name__ == '__main__':
    resolve()
