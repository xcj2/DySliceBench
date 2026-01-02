def binsearch(l, r, fn, i, j):
    while r - l > 1:
        m = (l + r) // 2
        if fn(m, i, j):
            l = m
        else:
            r = m
    return l

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    def fn(m, i, j):
        a = L[m]
        b = L[i]
        c = L[j]
        if a < b + c and b < c + a and c < a + b:
            return True
        return False
    r = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            if fn(j+1, i, j):
                r += binsearch(j+1, N, fn, i, j) - j
    return r
print(main())
