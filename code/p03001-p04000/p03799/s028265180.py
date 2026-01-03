import sys

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def solve():
    N, M = map(int, input().split())

    if 2*N >= M:
        ans = M // 2
    else:
        top = M // 2
        btm = 0

        while top - btm > 1:
            mid = (top + btm)//2
            if check(N + mid, M - 2*mid):
                btm = mid
            else:
                top = mid

        ans = N + btm

    print(ans)

def check(a, b):
    return 2*a <= b

if __name__ == '__main__':
    solve()