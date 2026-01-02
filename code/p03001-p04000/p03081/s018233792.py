#!/usr/bin/python3
N, Q = [int(x) for x in input().split()]
S = input()

qs = []
for _ in range(Q):
    t, d = [x for x in input().split()]
    #print(t, d)
    qs.append((t,-1 if d == 'L' else 1))

memo = [None] * N
memo.append(N)

def move(i):
    org = i
    if memo[i]:
        return memo[i]
    for t, d in qs:
        if S[i] == t:
            i+=d
        if i == -1:
            break
        elif i == N:
            break
    memo[org] = i
    return i

def search_right(lo, hi, x):
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if x < move(mid):
            hi = mid 
        else: # e <= t
            lo = mid +1
    return lo

def search_left(lo, hi, x):
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if move(mid) < x:
            lo = mid +1
        else: # e <= t
            hi = mid
    return lo


#l = search(0, N-1, -1)
#assert move(l) == 2, "%d" % move(l)
#print("search(-1)=", l)

l = search_right(0, N, -1)
r = search_left(0, N, N)

if 1==0:
    print(S)
    for t, d in qs:
        print(t, {-1:'L', 1:'R'}[d])
    m = [move(i) for i in range(N+1)]
    print(" ".join("%2d" % i for i in range(N+1)))
    print(" ".join("%+d" % x for x in m))
    print(" ".join(" *" if l == i else "  " for i in range(N+1)))
    print(" ".join(" *" if r == i else "  " for i in range(N+1)))

print(r-l)



