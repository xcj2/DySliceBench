def binsearch(l, r, fn):
    while r - l > 1:
        m = (l + r) // 2
        if fn(m):
            l = m
        else:
            r = m
    return l

def main():
    N, M, V, P = list(map(int, input().split()))
    A = sorted(list(map(int, input().split())), reverse=True)
    def ss(k):
        t = A[k] + M
        if A[P - 1] > t:
            return False
        r = M * (V - (N - k) - (P - 1))
        for i in range(P - 1, k):
            r -= min(M, max(0, t - A[i]))
            if r <= 0:
                return True
        return False
    return binsearch(P - 1, N, ss) + 1


print(main())
