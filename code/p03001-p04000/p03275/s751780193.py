NN = 18
N = int(input())
A = [int(a) for a in input().split()]

def chk(k):
    s = 0
    c = 0
    BIT=[0]*(2**NN+1)
    def add(i, x=1):
        i += 1 << NN - 1
        while i <= 2**NN:
            BIT[i] += x
            i += i & (-i)

    def getsum(i):
        ret = 0
        i += 1 << NN - 1
        while i != 0:
            ret += BIT[i]
            i -= i&(-i)
        return ret
    add(0)
    for i in range(N):
        if A[i] >= k:
            s += 1
        else:
            s -= 1
        c += getsum(s)
        add(s)
    if 4 * c >= N * (N+1):
        return 1
    return 0

l, r = 0, 1<<30
while r - l > 1:
    m = (l+r) // 2
    if chk(m):
        l = m
    else:
        r = m
print(l)
