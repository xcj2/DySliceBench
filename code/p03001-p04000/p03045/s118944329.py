def main():
    #Union Find
    #locate x 
    def find(x):
        if par[x] < 0:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    #merge x y
    def unite(x,y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        else:
            #sizeの大きいほうがx
            if par[x] > par[y]:
                x,y = y,x
            par[x] += par[y]
            par[y] = x
            return True
    #x and y in same group
    def same(x,y):
        return find(x) == find(y)
    
    #number of factor of x group
    def size(x):
        return -par[find(x)]

    n,m = map(int,input().split())
    #initiarize
    #根なら-size,子なら親の頂点
    par = [-1]*n

    for i in range(m):
        X,Y,Z = map(int,input().split())
        unite(X-1,Y-1)
    
    tank = set([])
    for i in range(n):
        tank.add(find(i))
    print(len(tank))

if __name__ == '__main__':
    main()