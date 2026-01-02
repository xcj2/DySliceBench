from itertools import combinations
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

def inversion(inds):
    bit = [0] * (N+1)
    def bit_add(x,w):
        while x <= N:
            bit[x] += w
            x += (x & -x)
    def bit_sum(x):
        ret = 0
        while x > 0:
            ret += bit[x]
            x -= (x & -x)
        return ret
    inv = 0
    for ind in reversed(inds):
        inv += bit_sum(ind + 1)
        bit_add(ind + 1, 1)
    return inv

INF = float('inf')
ans = INF
for odd_idxs in combinations(range(N), N//2):
    odd_idxset = set(odd_idxs)
    odds = []
    evens = []
    for i in range(N):
        if i in odd_idxset:
            odds.append((A[i] if i%2 else B[i], i))
        else:
            evens.append((B[i] if i%2 else A[i], i))
    odds.sort()
    evens.sort()
    vals = []
    inds = []
    for (e,ei),(o,oi) in zip(evens, odds):
        vals.append(e)
        vals.append(o)
        inds.append(ei)
        inds.append(oi)
    if len(evens) > len(odds):
        v,i = evens[-1]
        vals.append(v)
        inds.append(i)
    if any(a>b for a,b in zip(vals,vals[1:])): continue
    ans = min(ans, inversion(inds))

print(-1 if ans==INF else ans)