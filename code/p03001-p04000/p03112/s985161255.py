A, B, Q = [int(_) for _ in input().split()]
S = [int(input()) for i in range(A)]
T = [int(input()) for i in range(B)]
Q = [int(input()) for i in range(Q)]

#print(S, T, Q)

def calc_m(xs):
    return [(a + b) / 2 for a, b in zip(xs, xs[1:])]

sm = calc_m(S)
tm = calc_m(T)

#print(sm)
#print(tm)

import bisect

def calc_nearest_0(xs, y, ym):
    result = []
    i = 0
    for x in xs:
        while i < len(ym) and x >= ym[i]:
            i += 1
        result.append(y[i])
    return result

def calc_nearest(xs, y, ym):
    result = []
    for x in xs:
        i = bisect.bisect(ym, x)
        result.append(y[i])
    return result

sn = calc_nearest(S, T, tm)
tn = calc_nearest(T, S, sm)

#print(sn)
#print(tn)

def solve(q, S, T, sn, tn):
    nsp = bisect.bisect(S, q)
    ntp = bisect.bisect(T, q)

    rs = []

    if 0 <= nsp < len(S):
        rs.append(abs(S[nsp] - q) + abs(S[nsp] - sn[nsp]))
    nsp -= 1
    if 0 <= nsp < len(S):
        rs.append(abs(S[nsp] - q) + abs(S[nsp] - sn[nsp]))

    if 0 <= ntp < len(T):
        rs.append(abs(T[ntp] - q) + abs(T[ntp] - tn[ntp]))
    ntp -= 1
    if 0 <= ntp < len(T):
        rs.append(abs(T[ntp] - q) + abs(T[ntp] - tn[ntp]))

    # print("Q", q, S, T, sn, tn, r1, r2)
    return min(rs)

for q in Q:
    print(solve(q, S, T, sn, tn))
