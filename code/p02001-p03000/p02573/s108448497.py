n,m = map(int,input().split())
par = []
for i in range(n):
    par.append(-1)  #初期親
rank = [1 for i in range(n)] #初期ランク
cut = []
def find(n): #親検索andランク短縮
    global cut
    if par[n] < 0:
        for i in range(len(cut)):
            par[cut[i]] = n
        cut = []
        return n
    else:
        cut.append(n)
        find(par[n])
        return find(par[n])
def shorten(n): # 根に直接接続する
    global cut
    if par[n] < 0:
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
        par[y] += par[x]
        par[x] = y 
    elif rank[x] == rank[y]:
        par[x] += par[y]
        par[y] = x
        rank[x] += 1
    else:
        par[x] += par[y]
        par[y] = x
def judge(a,b):
    return par[a] == par[b]
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    unite(a,b)
ans = 0
for i in range(n):
    ans = max(ans,-par[i])
print(ans)