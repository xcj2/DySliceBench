N = int(input())
A = [int(a) for a in input().split()]
B = [int(a) for a in input().split()]
AB = sorted(list(set(A + B)))
D = {ab: i+1 for i, ab in enumerate(AB)}
A = [D[a] for a in A]
B = [D[a] for a in B]
def chk(L):
    NN = 5
    BIT=[0] * (2**NN+1)
    def addbit(i):
        while i <= 2**NN:
            BIT[i] += 1
            i += i & (-i)
 
    def getsum(i):
        ret = 0
        while i != 0:
            ret += BIT[i]
            i -= i&(-i)
        return ret
    s = 0
    for l in L[::-1]:
        s += getsum(l+1)
        addbit(l+1)
    return s
ans = 1 << 100
for m in range(1<<N):
    if bin(m).count("1") & 1: continue
    C = [[], []]
    for i in range(N):
        p = m >> i & 1
        q = p + i & 1
        C[q].append(((A[i] if p == 0 else B[i]) << 5) + i)
    if len(C[1]) != N // 2: continue
    C[0].sort()
    C[1].sort()
    CC = [C[i&1][i//2] for i in range(N)]
    for i in range(1, N):
        if CC[i-1] >> 5 > CC[i] >> 5: break
    else:
        CCC = [c % 32 for c in CC]
        ans = min(ans, chk(CCC))
print(ans if ans < 1 << 100 else -1)