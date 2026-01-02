# Union Find
#0オリジン以下注意

#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
    
def unite(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きい方がx
        if par[x] > par[y]:
            x, y = y, x
        par[x] += par[y] #ここで集合の個数を更新している
        par[y] = x
        return True
    
#xとyが同じ集合に含まれているかどうかを判定(同じ集合にあればTrue)
def same(x, y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]

#初期化
#根なら-size, 子なら親の頂点
################以下にコードを書く

while True:
    w, h = map(int, input().split())
    par = [-1]*(w*h)
    if (w, h) == (0, 0):
        break
    li = []
    for i in range(h):
        li.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w-1):
            if li[i][j] == li[i][j+1]:
                unite(w*i+j, w*i+j+1)
    for j in range(w):
        for i in range(h-1):
            if li[i][j] == li[i+1][j]:
                unite(w*i+j, w*i+j+w)
    for i in range(h):
        for j in range(w):
            I1 = i+1
            I2 = i-1
            J = j+1
            if 0 <= I1 and I1<h and 0<=J and J<w:
                if li[i][j] == 1 and li[I1][J] == 1:
                    unite(w*i+j, w*I1+J)
            if 0 <= I2 and I2<h and 0<=J and J<w:
                if li[i][j] == 1 and li[I2][J] == 1:
                    unite(w*i+j, w*I2+J)

                    
    #島を数える
    #陸のリスと
    li_riku = []
    for i in range(h):
        for j in range(w):
            if li[i][j]==1:
                li_riku.append(w*i+j)
    li_island = []
    sum_size = len(li_riku)
    for i in li_riku:
        k = find(i)
        if k not in li_island:
            li_island.append(k)
    print(len(li_island))
