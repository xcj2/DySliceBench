# -*- coding: utf-8 -*-

def main():
    #xの根を求める
    def find(x):
        if par[x] < 0:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    #xとyの属する集合の併合
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

    #xとyが同じ集合に属するかの判定
    def same(x,y):
        return find(x) == find(y)

    #xが属する集合の個数
    def size(x):
        return -par[find(x)]

    n, m =map(int, input().split())

    #初期化
    #根なら-size,子なら親の頂点
    par = [-1]*n
    #print(par)
    for i in range(m):
        A,B = map(int, input().split())
        unite(A-1,B-1)
    print(max([size(i) for i in range(n)]))


if __name__ == '__main__':
    main()
