def main():
    n,q = [int(i) for i in input().split()]
    #自分自身が親
    par = [ i for i in range(n)]
    #ランク
    rank = [ 0 for i in range(n)]
    #親を返す関数
    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]

    #木を結合する
    def unite(x,y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if rank[x]<rank[y]:
            par[x] = y
            return
        elif rank[y]<rank[x]:
            par[y] = x
            return
        else:
            par[x] = y
            rank[y] +=1
            return

    def same(x,y):
        return find(x) == find(y)

    for i in range(q):
        com,x,y = [int(j) for j in input().split()]
        #unite
        if com == 0:
            unite(x,y)
        #same
        else:
            if same(x,y):
                print(1)
            else:
                print(0)

if __name__ == '__main__':
    main()
