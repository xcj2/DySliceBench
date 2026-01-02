def binsearch(l, r, fn):
    while r - l > 1:
        m = (l + r) // 2
        if fn(m):
            l = m
        else:
            r = m
    return l

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = sorted(map(int, input().split()), reverse=True)
    AB = sorted((a + b for a in A for b in B), reverse=True)
    def helper(x):
        r = 0
        t = len(C) - 1
        for ab in AB:
            while t >= 0 and C[t] + ab < x:
                t -= 1
            r += t + 1
            if r >= K:
                return True
            if t < 0:
                return False
        return r >= K
    l = binsearch(AB[-1] + C[-1], AB[0] + C[0] + 1, helper)
    r = []
    t = len(C) - 1
    for ab in AB:
        while t >= 0 and C[t] + ab < l + 1:
            t -= 1
        if t < 0:
            break
        r.extend(ab + c for c in C[:t + 1])
    r.sort(reverse=True)
    r += [l] * (K - len(r))
    print('\n'.join(str(i) for i in r))

main()