import sys
input = sys.stdin.readline

N = int(input())
P = [0] * N
highest = 0
for n in range(N):
    P[n] = tuple([int(x) for x in input().strip().split()])
    highest = max(highest, P[n][2])

def calch(c, p):
    return max(c[2] - abs(p[0] - c[0]) - abs(p[1] - c[1]), 0)

def dh(c, p):
    return max(p[2] - (c[2] - abs(p[0] - c[0]) - abs(p[1] - c[1])), 0)

def f(p, P):
    h = -1
    th = -1
    for pp in P:
        if pp[2] == 0:
            if calch(p, pp) == 0:
                continue
            else:
                return -1
        th = dh(p, pp)
        if h == -1 or th == h:
            h = th
        else:
            return -1
    else:
        return th

for x in range(101):
    for y in range(101):
        h = highest
        while True:
            h_ = f((x, y, h), P)
            if h_ == -1:
                break
            elif h_ == 0:
                print(x, y, h)
                exit()
            else:
                h += h_