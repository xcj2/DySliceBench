def main():
    sx, sy, tx, ty = map(int, input().split())

    print(''.join(solve(sx, sy, tx, ty)))

def solve(sx, sy, tx, ty):
    for s in vertical(sx, sy, tx, ty): yield s
    for s in vertical(tx, ty, sx, sy): yield s
    yield 'L'
    for s in vertical(sx - 1, sy, tx, ty + 1): yield s
    yield 'D'
    yield 'R'
    for s in vertical(tx + 1, ty, sx, sy - 1): yield s
    yield 'U'

def vertical(sx, sy, tx, ty):
    yield move(ty - sy, 'U', 'D')
    yield move(tx - sx, 'R', 'L')

def move(q, up, down):
    if q > 0:
        return up * q
    else:
        return down * (-q)

main()
