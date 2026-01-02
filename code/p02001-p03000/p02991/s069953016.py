import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
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
        if aa == x[i+1]:
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

n,k = m()

s = [[] for i in range(n)]

sss = [[Max,Max,Max] for i in range(n)]

for i in range(k):
    u,v = m()
    u -= 1
    v -= 1
    if v not in s[u]:
        s[u].append(v)

st,g = m()
st -= 1
g -= 1
co = Max

eee = [[s,0,st,0]]
eee = cl.deque(eee)
def bfs(x,nn,now,coun):
    global eee,sss,g,co
    if sss[now][nn] == Max:
        if nn == 0 and g == now:
            co = min(co,coun)
        else:
            sss[now][nn] = coun
            if nn == 2:
                nn = 0
                coun += 1
            else:
                nn += 1
            for i in x[now]:
                eee.append([x,nn,i,coun])
    else:
        if now == g and nn == 0:
            co = min(co,coun)

while eee:
    op = eee.popleft()
    bfs(op[0],op[1],op[2],op[3])

#dfs(s,0,g,0)
if co == Max:
    print(-1)
else:
    print(co)

