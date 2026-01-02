def get_prime_factorized(N):
    R = []
    b, e = 2, 0
    while b ** 2 <= N:
        while N % b == 0:
            N  = N // b
            e += 1
        if e > 0:
            R.append([b, e])
        b, e = b + 1, 0
    if N > 1:
        R.append([N, 1])
    return R

def get_list_divisor(N, reverse=True):
    try:
        F = get_prime_factorized(N)
        L = re_func_divisior(F)
        R = []
        for l in L:
            for i, x in enumerate(l):
                if i == 0:
                    r = x
                else:
                    r *= x
            R.append(r)
        R.sort()
        if reverse == True:
            R.reverse()
    except:
        if N == 1:
            R = [1]
        else:
            R = [N]
    return R

def re_func_divisior(F):
    b, e = F.pop()
    P = re_func_divisior(F) if F else [[]]
    Q = [[b ** k] for k in range(e + 1)]
    return [p + q for p in P for q in Q]


N, M = map(int, input().split())

for d in get_list_divisor(M, reverse=True):
    if d * N <= M and M % d == 0:
        print(d)
        break
