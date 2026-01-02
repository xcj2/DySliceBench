import sys
sys.setrecursionlimit(10**7)

#debug = True
debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

def cumsum(x):
    y = []
    current = 0
    for i in x:
        y.append(current + i)
        current += i
    return y

def solve():
    n = int(input())
    lw = list(map(int, input().split()))

    cumw = cumsum(lw)
    s = cumw[-1]
    dprint(lw, cumw)
    mn = -1
    for left in cumw[:-1]:
        diff = abs(left - (s-left))
        dprint(s, s - left, mn, diff)
        if mn == -1 or mn > diff:
            mn = diff

    print(mn)

solve()