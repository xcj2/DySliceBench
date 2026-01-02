def solve(c, sushis):
    cw_maxs, cw_rets = create_accs(sushis, c, True)
    ccw_maxs, ccw_rets = create_accs(reversed(sushis), c, False)
    cw_max = cw_maxs[-1]
    ccw_max = ccw_maxs[-1]
    cw_ccw_max = turn_max(cw_rets, ccw_maxs)
    ccw_cw_max = turn_max(ccw_rets, cw_maxs)
    return max(cw_max, ccw_max, cw_ccw_max, ccw_cw_max)


def turn_max(rets, maxs):
    m = 0
    for i, r in enumerate(rets):
        ind = len(maxs) - 2 - i
        add = maxs[ind] if ind >= 0 else 0
        v = r + add
        if m < v:
            m = v
    return m


def create_accs(sushis, c, cw):
    maxs, vs_ret = [], []
    v_sum, v_max = 0, 0
    for d, v in sushis:
        v_sum += v
        dist = d if cw else c - d
        v_cur = v_sum - dist
        if v_max < v_cur:
            v_max = v_cur
        maxs.append(v_max)
        vs_ret.append(v_sum - dist*2)
    return maxs, vs_ret


n, c = map(int, input().split())
sushis = []
for _ in range(n):
    sushis.append([int(x) for x in input().split()])
print(solve(c, sushis))
