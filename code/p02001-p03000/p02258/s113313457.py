from sys import stdin
 
inf = 10**9 + 1

def solve():
    n = int(stdin.readline())
    R = [int(stdin.readline()) for i in range(n)]

    ans = max_profit(n, R)

    print(ans)

def max_profit(n, R):
    max_d = -inf
    min_v = R[0]

    for i in range(1, n):
        max_d = max(max_d, R[i] - min_v)
        min_v = min(min_v, R[i])

    return max_d

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None
 
if __name__ == '__main__':
    solve()