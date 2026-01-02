# damedatta
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
    D = sorted(map(int, input().split()), reverse=True)
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A = sorted((i + j for i in B for j in C), reverse=True)
    def calc(x):
        t = 0
        ii = len(D) - 1
        for i in A:
            while ii >= 0 and D[ii] + i < x:
                ii -= 1
            t += ii + 1
            if t >= K:
                return True
            if ii < 0:
                return False
        return t >= K
    l = binsearch(D[-1] + A[-1], D[0] + A[0]+1, calc)
    ii = len(D) - 1
    rl = []
    for i in A:
        while ii >= 0 and D[ii] + i < l + 1:
            ii -= 1
        if ii < 0:
            break
        rl.extend(i + j for j in D[:ii+1])
    rl.sort(reverse=True)
    rl += [l] * (K - len(rl))
    print('\n'.join(str(i) for i in rl))
main()
