import sys

inf = float('inf')

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def prim(n, As):
    checked = [False] * n
    d = [inf] * n
    checked[0] = True
    d[0] = 0
    nxt = 0
    tot_wgt = 0

    for i in range(n - 1):
        for j in range(n):
            if As[nxt][j] < d[j]:
                d[j] = As[nxt][j]

        min_w = inf
        min_n = 0
        for j in range(n):
            if not checked[j] and min_w > d[j]:
                min_w = d[j]
                min_n = j

        tot_wgt += min_w
        nxt = min_n
        checked[nxt] = True

    return tot_wgt

def solve():
    n = int(input())
    As = []

    for i in range(n):
        line = [int(j) for j in input().split()]
        As.append([i if i != -1 else inf for i in line])

    ans = prim(n, As)

    print(ans)


if __name__ == '__main__':
    solve()