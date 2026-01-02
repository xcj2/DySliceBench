import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

from heapq import heappush, heappop

t = n_in()

for _ in range(t):
    n = n_in()

    sheeps = []
    for i in range(n):
        k,l,r = l_in()
        sheeps.append((i,k-1,l,r))


    res = 0
    base = 0

    memo = []
    for i in range(n):
        memo.append(set())

    base = 0
    for i,k,l,r in filter(lambda x: x[2] > x[3], sheeps):
        memo[k].add(i)
        base += r

    res += base

    q = []
        
    for pos in range(n):
        for s in memo[pos]:
            _,k,l,r = sheeps[s]
            heappush(q, (l-r, s))

        while len(q) > pos+1:
            heappop(q)

    for delta, i in q:
        res += delta

        
    memo = [set() for _ in range(n+1)]

    base = 0
    for i,k,l,r in filter(lambda x: x[2] <= x[3], sheeps):
        memo[k+1].add(i)
        base += l

    res += base

    q = []
        
    for pos in reversed(range(n)):
        for s in memo[pos]:
            _,k,l,r = sheeps[s]
            heappush(q, (r-l, s))

        while len(q) > n-pos:
            heappop(q)
    for delta, i in q:
        res += delta

    print(res)

    
        
