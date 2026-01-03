import sys

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def solve():
    H, W, N = map(int, sys.stdin.readline().split())
    nb = [0] * 10
    bm = dict()
    bb = set()

    for lp in range(N):
        a, b = map(int, sys.stdin.readline().split())
        a, b = a-1, b-1
        res = search(H, W, bm, bb, a, b)

        if 1 <= a <= H-2 and 1 <= b <= W-2:
            bm[a,b] = 1 + res
        
        bb.add((a,b))

    # debug(bm, locals())
    for i in bm.values():
        nb[i] += 1

    nb[0] = (H-2)*(W-2) - sum(nb)

    print(*nb, sep='\n')

def search(H, W, bm, bb, a, b):
    res = 0
    dx = (1, 0, -1, 0, 1, 1, -1, -1)
    dy = (0, 1, 0, -1, 1, -1, 1, -1)

    for j in range(8):
        if (a + dx[j], b + dy[j]) in bb:
            res += 1

        if a + dx[j] < 1 or a + dx[j] > H - 2:
            continue
        if b + dy[j] < 1 or b + dy[j] > W - 2:
            continue

        if (a + dx[j], b + dy[j]) not in bm:
            bm[a + dx[j], b + dy[j]] = 0

        bm[a + dx[j], b + dy[j]] += 1

    return res

if __name__ == '__main__':
    solve()