
def factorize(n):
    nn = n
    lst = []
    for i in range(2, int(1 + n ** 0.5)):
        k = 0
        while nn % i == 0:
            k += 1
            nn = nn // i
        if k > 0:
            lst.append([i, k])
    if nn != 1:
        lst.append([nn, 1])
    return lst

def gen_divisor(m):
    # not sorted!
    yield 1
    factorized = factorize(m)
    length = len(factorized)
    if length == 0:
        return
    factor_nexps = [0] * length
    while True:
        # increment
        factor_nexps[0] += 1
        for idx in range(length - 1):
            if factor_nexps[idx] > factorized[idx][1]:
                factor_nexps[idx] = 0
                factor_nexps[idx+1] += 1
        if factor_nexps[-1] > factorized[-1][1]:
            return
        divisor = 1
        for i, tup in enumerate(factorized):
            divisor *= tup[0] ** factor_nexps[i]
        yield divisor

N, M = map(int, input().split())

def solve():
    divisors = sorted([di for di in gen_divisor(M) if di >= N])
    ans = M // divisors[0]
    return ans

print(solve())

