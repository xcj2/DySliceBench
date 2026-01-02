def find(x):
    if(p[x] == x):return x
    else: 
        p[x] = find(p[x])
        return p[x]
def unite(x,y):
    x = find(x)
    y = find(y)

    if x==y:return
    if rank[x] < rank[y]:
        p[x] = y
    else:
        p[y] = x
        if rank[x] == rank[y]:
            rank[x]+=1

def same(x,y):
    if find(x) == find(y):
        return 1
    else: return 0

if __name__=='__main__':
    n, q = (int(x) for x in input().split())
    p = [i for i in range(n)]
    rank = [0 for i in range(n)]
        
    for i in range(q):
        com, x, y = (int(x) for x in input().split())
        if com == 0:unite(x,y)
        else:print(same(x,y))

