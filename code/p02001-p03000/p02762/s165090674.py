n,m,k = map(int,input().split())
import collections
par = []
for i in range(n):
    par.append(i)  #初期親
rank = [1 for i in range(n)] #初期ランク
flist = [[] for i in range(n)]
blist = [[] for i in range(n)]
cut = []
def find(n): #親検索andランク短縮
    global cut
    if par[n] == n:
        for i in range(len(cut)):
            par[cut[i]] = n
        cut = []
        return n
    else:
        cut.append(n)
        find(par[n])
        return find(par[n])
def shorten(n): # ランクを2にする
    global cut
    if par[n] == n:
        for i in range(len(cut)):
            par[cut[i]] = n
        cut = []
    else:
        cut.append(n)
        shorten(par[n])
def unite(a,b): #グループ併合
    x = find(a)
    y = find(b) #根っこ同士をくっつける
    if x == y: 
        return    #既に同一ユニオンなら何もしない
    if rank[x] < rank[y]:
        par[x] = y 
    elif rank[x] == rank[y]:
        par[y] = x
        rank[x] += 1
    else:
        par[y] = x
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    flist[a].append(b)
    flist[b].append(a)
    unite(a,b)
for i in range(n):
    shorten(i)
for i in range(k):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    if par[a] == par[b]:
        blist[a].append(b)
        blist[b].append(a)
c = collections.Counter(par)
for i in range(n):
    ans = c[par[i]] -len(flist[i])-len(blist[i])-1
    print(ans,end = ' ')