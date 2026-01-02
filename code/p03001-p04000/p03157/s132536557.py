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
    
h, w = map(int,input().split())
s = [["dammy"] * (w+2)]
for i in range(h):
    s.append(["dammy"]+list(input())+["dammy"])
s.append(["dammy"] * (w+2))

par = [i for i in range(h*w+1)] #index調整
rank = [1] * (h*w+1) #index調整

for i in range(1,h+1):
    for j in range(1,w+1):
        index = w*(i-1)+j
        if s[i][j] == "#": #黒
            if s[i-1][j] == ".":
                unite(index, index-w, par, rank)
            if s[i+1][j] == ".":
                unite(index, index+w, par, rank)
            if s[i][j-1] == ".":
                unite(index, index-1, par, rank)
            if s[i][j+1] == ".":
                unite(index, index+1, par, rank)
        elif s[i][j] == ".": #白
            if s[i-1][j] == "#":
                unite(index, index-w, par, rank)
            if s[i+1][j] == "#":
                unite(index, index+w, par, rank)
            if s[i][j-1] == "#":
                unite(index, index-1, par, rank)
            if s[i][j+1] == "#":
                unite(index, index+1, par, rank)

bw = [[0,0] for i in range(h*w+1)]
parset = set()

for i in range(1,h+1):
    for j in range(1, w+1):
        index = w*(i-1)+j
        parent = find(index,par)
        if not parent in parset:
            parset.add(parent)
        if s[i][j] == "#":
            bw[parent][0] += 1
        elif s[i][j] == ".":
            bw[parent][1] += 1

ans = 0

for i in list(parset):
    ans += (bw[i][0] * bw[i][1])
    
print(ans)