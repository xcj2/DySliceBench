import numpy as np


def get_prime_factorized(N):
    result    = []
    base, exp = 2, 0
    while base ** 2 <= N:
        while N % base == 0:
            N    = N // base
            exp += 1
        if exp > 0:
            result.append([base, exp])
        base, exp = base + 1, 0
    if N > 1:
        result.append([N, 1])
    return result

def re_func_divisior(prime_factorized):
    base, exp = prime_factorized.pop()
    P = re_func_divisior(prime_factorized) if prime_factorized else [[]]
    Q = [[base ** k] for k in range(exp + 1)]
    return [p + q for p in P for q in Q]

def get_list_divisor(N, reverse=True):
    try:
        prime_factorized = get_prime_factorized(N)
        res    = re_func_divisior(prime_factorized)
        result = []
        for k in res:
            for i, x in enumerate(k):
                if i == 0:
                    r = x
                else:
                    r *= x
            result.append(r)
        result = sorted(result, reverse=reverse)
    except:
        result = [N]
    return result


N, K = map(int, input().split())
A    = list(map(int, input().split()))

X = get_list_divisor(sum(A))

is_break = False

for x in X:
    POS = sorted([a % x for a in A if a % x != 0])
    NEG = [x - pos for pos in POS]
    POS_cumsum = np.cumsum(POS)
    NEG_cumsum = np.cumsum(NEG[::-1])[::-1]
    for sep in range(1, len(POS)):
        if POS_cumsum[sep-1] == NEG_cumsum[sep] and POS_cumsum[sep-1] <= K:
            is_break = True
            break
    if is_break:
        break

print(x)
