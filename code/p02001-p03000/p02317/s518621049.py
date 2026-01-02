from sys import stdin

def solve():
    n = int(stdin.readline())
    A = [int(stdin.readline()) for i in range(n)]

    inf = 10**9 + 1
    dp = [inf] * n

    for a in A:
        j = nibutan(dp, a)
        dp[j] = a

    for i, v in enumerate(dp):
        if v == inf:
            print(i)
            return

    print(n)

def nibutan(dp, a):
    btm = -1
    top = len(dp)

    while top - btm > 1:
        mid = (top + btm) // 2
        if dp[mid] >= a:
            top = mid
        else:
            btm = mid

    assert 0 <= top < len(dp)
    return top

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

if __name__ == '__main__':
    solve()