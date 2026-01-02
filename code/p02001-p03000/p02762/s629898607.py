#Union Find
n,m,k=map(int, input().split())

#xの根を求める, #parents[i]＝h　はiの親はjという意味、parents[i]=iはiが根という意味
def find(x):
    if parents[x] < 0: # 負なら根
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]
    
#xとyの属する集合の併合
def unite(x,y):
    x = find(x) # x,yは根の番号にする。
    y = find(y)
    
    if x == y:
        return False
    else:
        if parents[x] > parents[y]: # sizeの大きいほうがx
            x,y = y,x
        parents[x] += parents[y]
        parents[y] = x
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)


#xが属する集合の個数
def size(x):
    return -parents[find(x)]

#初期化
#根なら-size,子なら親の頂点
parents=[-1]*n

friend = [set() for _ in range(n)]

for i in range(m): # 友達リスト
    a,b=map(int,input().split())
    unite(a-1,b-1)
    friend[a-1].add(b-1)
    friend[b-1].add(a-1)
    
a=[size(i)-len(friend[i])-1 for i in range(n)]

for i in range(k):
    c,d=map(int,input().split())
    if same(c-1,d-1):
        a[c-1]-=1
        a[d-1]-=1
print(*a)