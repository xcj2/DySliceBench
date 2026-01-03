import sys

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def solve():
    N, K = map(int, input().split())
    D = [str(i) for i in input().split()]
    ans = 0

    for m in range(N, 10**6):
        if canbuy(N, D, m):
            ans = m
            break

    print(m)

def canbuy(N, D, m):
    m = str(m)

    for d in D:
        if m.find(str(d)) != -1:
            return False

    return True


if __name__ == '__main__':
    solve()