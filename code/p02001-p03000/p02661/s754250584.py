import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

n=n_in()

from collections import defaultdict

memo=defaultdict(list)
for i in range(n):
    a,b=l_in()
    memo[a].append((i,True))
    memo[b].append((i,False))
    


left=set()
mid=set()
right=set(range(n))


lazy=set()

res_left=-1
res_right=-1

res2_left=-1
res2_right=-1

for x in sorted(memo.keys()):
    for i in lazy:
        mid.remove(i)
        left.add(i)
    lazy.clear()
    
    for i, is_a in memo[x]:
        if is_a:
            right.remove(i)
            mid.add(i)
        else:
            lazy.add(i)
            
    if n%2 == 0:
        m = n//2-1

        # n//2
        if len(mid) >= 1 and len(left) <= m and len(right) <= m+1:
            if res_left == -1:
                res_left = x
            res_right = x
            
        # n//2 + 1
        if len(mid) >= 1 and len(left) <= m+1 and len(right) <= m:
            if res2_left == -1:
                res2_left = x
            res2_right = x
    else:
        m = (n-1)//2
        if len(mid) >= 1 and len(left) <= m and len(right) <= m:
            if res_left == -1:
                res_left = x
            res_right = x

if n%2 == 0:
    print(res_right-res_left+res2_right-res2_left+1)
else:
    print(res_right-res_left+1)
