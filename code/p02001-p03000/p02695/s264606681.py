import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,m,q = map(int,readline().split())
lst1 = []
for i in range(q):
    a,b,c,d = map(int,readline().split())
    lst1.append([a-1,b-1,c,d])

def func(lst):
    res = 0
    for a,b,c,d in lst1:
        if lst[b]-lst[a] == c:
            res += d
    return res
lst2 = []
def func2(lst,now,num):
    if now == -1:
        lst2.append(lst)
        return
    else:
        for i in range(1,num+1):
            res = lst.copy()
            res[now] = i
            func2(res,now-1,i)

func2([1]*n,n-1,m)

def dfs(lst):
    ans = 0
    for i in lst2:
        ans = max(ans,func(i))
    return ans

print(dfs([1]*n))