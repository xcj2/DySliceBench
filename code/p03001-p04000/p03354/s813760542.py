#!/mnt/c/Users/moiki/bash/env/bin/python
N,M = map(int, input().split())
p = list(map(int, input().split()))
swappair= [list(map(int, input().split())) for _ in range(M)]

union_list = [-1 for _ in range(N+1)]

def find(a): # get root
    while not union_list[a] == -1:
        a = union_list[a]
    return a

def merge(a,b): 
    ia = find(a)
    ib = find(b)
    if ia == ib:
        return 
        
    if ia < ib:
        union_list[ib] = ia
    elif ia > ib:
        union_list[ia] = ib
    


def is_same_grp(a,b):
    ia = find(a)
    ib = find(b)
    return ia == ib

for i in range(M):
    merge(*swappair[i])

ans = 0
for i in range(1,N+1):
    ans += int( is_same_grp(i, p[i-1]))

print(ans)


