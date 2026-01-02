def binsearch(l, r, fn):
    while r - l > 1:
        m = (l + r) // 2
        if fn(m):
            l = m
        else:
            r = m
    return l

def main():
    N, Q = map(int, input().split())
    s = input()
    TD = [input().split() for _ in range(Q)]
    def die(n):
        if n < 0:
            return -1
        if n >= N:
            return 1
        for t, d in TD:
            if s[n] != t:
                continue
            if d == 'L':
                n -= 1
                if n < 0:
                    return -1
            else:
                n += 1
                if n >= N:
                    return 1
        return 0
    L = binsearch(-1, N, lambda x: die(x) == -1)
    R = binsearch(-1, N, lambda x: die(x) != 1)
    return R - L

print(main())
