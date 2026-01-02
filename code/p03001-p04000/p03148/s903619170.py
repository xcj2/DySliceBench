from collections import defaultdict
import heapq


def get_first_try(K, ts, ds):
    eats = []
    non_eats = []
    for i in range(len(ts)):
        t = ts[i]
        d = ds[i]
        heapq.heappush(eats, (d, t))
        if len(eats) > K:
            non_eats.append(heapq.heappop(eats))
    return [(t, d) for d,t in eats], [(t, d) for d,t in non_eats]

def count_kinds(eats):
    kinds = defaultdict(int)
    for e in eats:
        kinds[e[0]] += 1
    return kinds

def calc_satisfaction(eats, eat_kinds):
    s = 0
    for e in eats:
        s += e[1]
    return s + calc_bonus(eat_kinds)


def calc_bonus(kinds):
    x = 0
    for k in kinds:
        if kinds[k] > 0:
            x += 1
    return x**2


def solve(N, K, ts, ds):
    eats, non_eats = get_first_try(K, ts, ds)
    eat_kinds = count_kinds(eats)
    satisfaction = calc_satisfaction(eats, eat_kinds)
    sorted_eats = sorted(eats, key=lambda x: x[1])
    sorted_non_eats = sorted(non_eats, key=lambda x: x[1], reverse=True)
    n_kinds = len(eat_kinds)

    max_satisfaction = satisfaction

    i = 0
    j = 0
    while i < len(sorted_eats) and j < len(sorted_non_eats):
        t, d = sorted_eats[i]
        if eat_kinds[t] == 1:
            i += 1
            continue
        t2, d2 = sorted_non_eats[j]
        if eat_kinds[t2] > 0:
            j += 1
            continue
        prev_bonus = n_kinds ** 2
        eat_kinds[t] -= 1
        eat_kinds[t2] += 1
        n_kinds += 1
        current_bonus = n_kinds ** 2
        satisfaction = satisfaction - d + d2 - prev_bonus + current_bonus
        if max_satisfaction < satisfaction:
            max_satisfaction = satisfaction
        i += 1
        j += 1

    return max_satisfaction


N, K = list(map(int, input().split(' ')))

ts = []
ds = []
for i in range(N):
    t, d = list(map(int, input().split(' ')))
    ts.append(t)
    ds.append(d)

print(solve(N, K, ts, ds))