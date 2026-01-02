from itertools import combinations, chain

H, W, K = map(int, input().split())
Sss = []
for _ in range(H):
    Sss.append(list(map(int, input())))


def h_divide(Sss, div_is):
    result = []
    for s, e in zip(chain([0], div_is), chain(div_is, [len(Sss)])):
        result.append(Sss[s:e])
    return result


def _v_end(Sss, start, K):
    count = 0
    for i in range(start, len(Sss[0])):
        s = sum(map(lambda Ss: Ss[i], Sss))
        if count + s > K:
            return i - 1
        count += s
    return len(Sss[0]) - 1


def v_end(Ssss, start, K):
    result = -1
    for Sss in Ssss:
        end = _v_end(Sss, start, K)
        if end < start:
            return -1
        if result < 0 or result > end:
            result = end
    return result


def v_div_count(Ssss, K):
    start, result = 0, 0
    while True:
        end = v_end(Ssss, start, K)
        if end < 0:
            return -1
        if end == len(Ssss[0][0]) - 1:
            break
        result += 1
        start = end + 1
    return result


h_cands = list(range(1, len(Sss)))
ans = -1
for n in range(len(h_cands) + 1):
    for comb in combinations(h_cands, n):
        if ans > 0 and n >= ans:
            continue
        Ssss = h_divide(Sss, list(comb))
        cnt = v_div_count(Ssss, K)
        if cnt < 0:
            continue
        if ans < 0 or ans > n + cnt:
            ans = n + cnt
print(ans)
