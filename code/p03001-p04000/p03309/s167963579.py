def binsearch(l, r, fn):
    while r - l > 1:
        m = (l + r) // 2
        if fn(m):
            l = m
        else:
            r = m
    return l

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(a - i for i, a in enumerate(A, 1))
    def h(t):
        return sum(abs(a - t) for a in A)
    l = A[0]
    r = A[-1]
    while r - l > 1:
        m = (l + r) // 2
        t = h(m + 1) - h(m)
        if t == 0:
            return h(m)
        if t < 0:
            l = m + 1
        else:
            r = m
    return min(h(l), h(r))

print(main())
