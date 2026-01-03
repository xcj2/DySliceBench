h, w = map(int, input().split())

# x,yの左からv列を縦に割って、左側を真ん中で横に割った時の答え
def calc(x, y, v):
    c = [v*(y//2), v*(y-y//2), (x-v)*y]
    c.sort()
    return c[2]-c[0]

# 縦横に割った時の差の最小値
def cut(x, y):
    lo = 0
    hi = x
    while hi-lo > 2:
        mid = (hi+lo)//2
        r1 = calc(x, y, mid)
        r2 = calc(x, y, mid+1)
        if r1 < r2:
            hi = mid+1
        else:
            lo = mid
    return min(calc(x, y, hi), calc(x, y, lo), calc(x, y, (hi+lo)//2))

def solve(x, y):
    # 縦横に割った時の最小値と縦だけに割った時の小さい方
    return min(cut(x, y), y)

def Solve(h, w):
    if h*w%3 == 0:
        return 0
    return min(solve(h, w), solve(w, h))

print(Solve(h, w))
