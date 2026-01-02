h,w = map(int,input().split())
s = [None]*h
for i in range(h):
    s[i]=list(input())
    
###########
#Union Find
par = [] #親
rank = [] #木の深さ

#初期化
for i in range(h*w):
    #par[i]:i rank[i]:0
    par.append(i)
    rank.append(0)

#木の根を求める
def find(x,par):
    if par[x] == x:
        return x
    else:
        return find(par[x],par)

#xとyの属する集合の併合
def unite(x,y,par,rank):
    x = find(x,par)
    y = find(y,par)
    
    if x != y:
        #xとyの属している集合が異なる時
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x]==rank[y]:
                rank[x] += 1

#xとyが同じ集合に属するかの判定
def same(x,y,par):
    return find(x,par) == find(y,par)
###############
for i in range(h*w):
    if i//w + 1 < h and s[i//w][i%w] != s[i//w+1][i%w]:
        unite(i,i+w,par,rank)
    if i%w +1 < w and s[i//w][i%w] != s[i//w][i%w+1]:
        unite(i,i+1,par,rank)

res = [[0,0] for i in range(w*h)] #[".","#"]
for i in range(h*w):
    r = find(i,par)
    if s[i//w][i%w] ==".":
        res[r][0]+=1
    else:
        res[r][1]+=1

ans = 0
for i in range(h*w):
    ans += res[i][0]*res[i][1]
print(ans)