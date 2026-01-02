import sys,bisect as bs,collections as cl,heapq as hq
sys.setrecursionlimit(100000)
mod = 10**9+7
Max = sys.maxsize
def l(): #intのlist
    return list(map(int,input().split()))
def m(): #複数文字
    return map(int,input().split())
def onem(): #Nとかの取得
    return int(input())
def s(x): #圧縮
    a = []
    aa = x[0]
    su = 1
    for i in range(len(x)-1):
        if aa != x[i+1]:
            a.append([aa,su])
            aa = x[i+1]
            su = 1
        else:
            su += 1
    a.append([aa,su])
    return a
def jo(x): #listをスペースごとに分ける
    return " ".join(map(str,x))
def max2(x): #他のときもどうように作成可能
    return max(map(max,x))
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False

n,q = m()

data = [l() for i in range(q)]

edges = [[] for i in range(n)]

for a,b,c in data:
    edges[a-1].append([b-1,c])
    edges[b-1].append([a-1,-c])

num = [0 for _ in range(n)]

Ma,mi = 0,0

vi = [False for i in range(n)]
ans = 0

for i in range(n):
    if vi[i]:
        continue
    stack = [i]
    vi[i] = True
    while stack:
        v = stack.pop()
        for e,r in edges[v]:
            if not vi[e]:
                num[e] = num[v] + r
                stack.append(e)
                vi[e] = True

for i in range(n):
    if num[i] < mi:
        mi = num[i]
    elif num[i] > Ma:
        Ma = num[i]
    for e,r in edges[i]:
        if num[i] + r != num[e]:
            ans = -1
            break
    else:
        continue
    break
else:
    print("Yes")
    exit()
print("No")





