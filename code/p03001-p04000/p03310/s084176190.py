#dame datta
def binsearch(l, r, fn):
    while r - l > 1:
        m = (l + r) // 2
        t = fn(m+1) - fn(m)
        if t == 0:
            return fn(m)
        if t < 0:
            l = m + 1
        else:
            r = m
    if fn(l) < fn(r):
        return l
    else:
        return r
def main():
    N = int(input())
    A = list(map(int, input().split()))
    Al = [A[0]]
    r = (10**9)*(2*(10**5))
    for i in A[1:]:
        Al.append(Al[-1] + i)
    for t in range(2, N-1):
        def fn1(i):
            return abs(Al[t-1] - Al[i-1] - Al[i-1])
        t1 = binsearch(1, t, fn1)
        def fn2(i):
            return abs(Al[-1] - Al[i-1] - Al[i-1] + Al[t-1])
        t2 = binsearch(t+1, N, fn2)
        x = Al[-1] - Al[t2-1]
        y = Al[t2-1] - Al[t-1]
        z = Al[t-1] - Al[t1-1]
        w = Al[t1-1]
        r = min(max(x,y,z,w) - min(x,y,z,w), r)
    return r
print(main())
