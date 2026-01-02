import sys
input = sys.stdin.readline

def count(P):
    res = 0
    #A1 ... AnのBIT(1-indexed)
    BIT = [0]*(N+1)

    #A1 ~ Aiまでの和 O(logN)
    def BIT_query(idx):
        res_sum = 0
        while idx > 0:
            res_sum += BIT[idx]
            idx -= idx&(-idx)
        return res_sum

    #Ai += x O(logN)
    def BIT_update(idx,x):
        while idx <= N:
            BIT[idx] += x
            idx += idx&(-idx)
        return


    Pi = [None]*N
    for i in range(N):
        Pi[P[i]] = i
    for i in range(N):
        p = Pi[i]
        res += i-BIT_query(p+1)
        BIT_update(p+1, 1)
    return res
 

N = int(input())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))
uhalf = -(-N//2)
dhalf = N - uhalf
inf = 10**9+7
ans = inf
for S in range(1<<N):
    card = [A[i] if S&(1<<i) else B[i] for i in range(N)]
    parity = [(1&(S>>i))^(i&1) for i in range(N)]
    even = [(card[i], i) for i in range(N) if parity[i]]
    odd = [(card[i], i) for i in range(N) if not parity[i]]
    if len(even) != uhalf or len(odd) != dhalf:
        continue
    even.sort()
    odd.sort()
    if any(e[0] > o[0] for e, o in zip(even, odd)) or any(e[0] < o[0] for e, o in zip(even[1:], odd)):
        continue
    perm = [even[i//2][1] if not i&1 else odd[i//2][1] for i in range(N)]
    ans = min(ans, count(perm))
print(ans if ans < inf else -1)
