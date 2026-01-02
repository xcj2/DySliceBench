N, K, *A = map(int, open(0).read().split())

neg = sorted([-a for a in A if a < 0])
pos = sorted([a for a in A if a >= 0])

def _count_pair_neg(x):
    x = -x
    res = 0

    MAX = len(pos)
    i = 0
    for n in reversed(neg):
        while i < MAX and n * pos[i] < x:
            i += 1
            
        res += MAX - i
    return res


def _count_pair_pos(x):
    res = 0

    # Negative list
    i = 0
    MAX = len(neg)
    for n in reversed(neg):
        if n * n <= x:
            res -= 1
            
        while i < MAX and neg[i] * n <= x:
            i += 1
        res += i
        
    # Positive list
    i = 0
    MAX = len(pos)
    for n in reversed(pos):
        if n * n <= x:
            res -= 1
            
        while i < MAX and pos[i] * n <= x:
            i += 1
        res += i
        
    # Devide by 2 for counting the same pair twice
    res //= 2
    res += len(neg) * len(pos)
    return res


def count_pair(x):
    if x < 0:
        return _count_pair_neg(x)
    
    return _count_pair_pos(x)


# Bounds
lb = 0
ub = 2 * 10 ** 18 + 2

while ub - lb > 1:
    mid = (ub + lb) // 2
    if count_pair(mid - 10 ** 18 - 1) < K:
        lb = mid
    else:
        ub = mid

print(ub - 10 ** 18 - 1)
