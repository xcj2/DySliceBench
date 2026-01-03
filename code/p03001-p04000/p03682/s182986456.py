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
n = onem()
data = []
edges = []
for i in range(n):
    kkk = l()
    data.append([i]+ kkk)
ddd = sorted(data,key = lambda x:x[1])
bbb = sorted(data,key = lambda x:x[2])

Ne = cl.defaultdict(list)
for i in range(1,n):
    Ne[ddd[i-1][0]].append((ddd[i][0],ddd[i][1]-ddd[i-1][1]))
    Ne[ddd[i][0]].append((ddd[i-1][0],ddd[i][1]-ddd[i-1][1]))
    Ne[bbb[i-1][0]].append((bbb[i][0],bbb[i][2]-bbb[i-1][2]))
    Ne[bbb[i][0]].append((bbb[i-1][0],bbb[i][2]-bbb[i-1][2]))

is_used = [False for i in range(n+1)]
h = []
hq.heappush(h,(0,1))
ans = 0

while h:
    d,n = hq.heappop(h)
    if is_used[n]:
        continue
    ans += d
    is_used[n] = True
    for z,x in Ne[n]:

        if not is_used[z]:
            hq.heappush(h,(x,z))

print(ans)



