n = int(input())
info = [list(input().split()) for i in range(n)]
for i in range(n):
    x, y, dire = info[i]
    info[i] = (int(x), int(y), dire)
INF = 10 ** 18


def solve_x(mid, op=max, e=-INF):
    # mid秒後のxの位置: x0
    # mid+1秒後のxの位置: x1
    x0, x1 = e, e
    for x, _, dire in info:
        if dire == "U" or dire == "D":
            x0, x1 = op(x, x0), op(x, x1)
        elif dire == "R":
            x0, x1 = op(x + mid, x0), op(x + mid + 1, x1)
        else:
            x0, x1 = op(x - mid, x0), op(x - mid - 1, x1)
    return x0, x1


def solve_y(mid, op=max, e=-INF):
    # mid秒後のyの位置: y0
    # mid+1秒後のyの位置: y1
    y0, y1 = e, e
    for _, y, dire in info:
        if dire == "L" or dire == "R":
            y0, y1 = op(y, y0), op(y, y1)
        elif dire == "U":
            y0, y1 = op(y + mid, y0), op(y + mid + 1, y1)
        else:
            y0, y1 = op(y - mid, y0), op(y - mid - 1, y1)
    return y0, y1


def solve_s(t):
    """時刻tにおける面積sを求める"""
    x_max = -INF * INF
    x_min = INF * INF
    y_max = -INF * INF
    y_min = INF * INF
    for x, y, dire in info:
        if dire == "L":
            x_max = max(x - t, x_max)
            x_min = min(x - t, x_min)
            y_max = max(y, y_max)
            y_min = min(y, y_min)
        if dire == "R":
            x_max = max(x + t, x_max)
            x_min = min(x + t, x_min)
            y_max = max(y, y_max)
            y_min = min(y, y_min)
        if dire == "D":
            x_max = max(x, x_max)
            x_min = min(x, x_min)
            y_max = max(y - t, y_max)
            y_min = min(y - t, y_min)
        if dire == "U":
            x_max = max(x, x_max)
            x_min = min(x, x_min)
            y_max = max(y + t, y_max)
            y_min = min(y + t, y_min)
    return (x_max - x_min) * (y_max - y_min)
            
            
ts = set([])
# xmaxについて
# 単調減少 → 不変
ok = -1
ng = INF
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    x0, x1 = solve_x(mid, op=max, e=-INF)
    if x0 > x1:
        ok = mid
    else:
        ng = mid
ts.add(ok - 2), ts.add(ok - 1), ts.add(ok), ts.add(ng), ts.add(ng + 1), ts.add(ng + 2)
# 不変 → 単調増加
ok = -1
ng = INF
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    x0, x1 = solve_x(mid, op=max, e=-INF)
    if x0 < x1:
        ng = mid
    else:
        ok = mid
ts.add(ok - 2), ts.add(ok - 1), ts.add(ok), ts.add(ng), ts.add(ng + 1), ts.add(ng + 2)

# xminについて
# 単調増加 → 不変
ok = -1
ng = INF
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    x0, x1 = solve_x(mid, op=min, e=INF)
    if x0 < x1:
        ok = mid
    else:
        ng = mid
ts.add(ok - 2), ts.add(ok - 1), ts.add(ok), ts.add(ng), ts.add(ng + 1), ts.add(ng + 2)
# 不変 → 単調減少
ok = -1
ng = INF
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    x0, x1 = solve_x(mid, op=min, e=INF)
    if x0 > x1:
        ng = mid
    else:
        ok = mid
ts.add(ok - 2), ts.add(ok - 1), ts.add(ok), ts.add(ng), ts.add(ng + 1), ts.add(ng + 2)


# ymaxについて
# 単調減少 → 不変
ok = -1
ng = INF
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    y0, y1 = solve_y(mid, op=max, e=-INF)
    if y0 > y1:
        ok = mid
    else:
        ng = mid
ts.add(ok - 2), ts.add(ok - 1), ts.add(ok), ts.add(ng), ts.add(ng + 1), ts.add(ng + 2)
# 不変 → 単調増加
ok = -1
ng = INF
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    y0, y1 = solve_y(mid, op=max, e=-INF)
    if y0 < y1:
        ng = mid
    else:
        ok = mid
ts.add(ok - 2), ts.add(ok - 1), ts.add(ok), ts.add(ng), ts.add(ng + 1), ts.add(ng + 2)

# yminについて
# 単調増加 → 不変
ok = -1
ng = INF
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    y0, y1 = solve_y(mid, op=min, e=INF)
    if y0 < y1:
        ok = mid
    else:
        ng = mid
ts.add(ok - 2), ts.add(ok - 1), ts.add(ok), ts.add(ng), ts.add(ng + 1), ts.add(ng + 2)
# 不変 → 単調減少
ok = -1
ng = INF
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    y0, y1 = solve_y(mid, op=min, e=INF)
    if y0 > y1:
        ng = mid
    else:
        ok = mid
ts.add(ok - 2), ts.add(ok - 1), ts.add(ok), ts.add(ng), ts.add(ng + 1), ts.add(ng + 2)


ans = INF * INF
for t in ts:
    if t >= INF - 10:
        continue
    if t - 0.5 >= 0:
        ans = min(solve_s(t - 0.5), ans)
    if t >= 0:
        ans = min(solve_s(t), ans)
    if t + 0.5 >= 0:
        ans = min(solve_s(t + 0.5), ans)
print(ans)