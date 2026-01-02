def main():
    import sys,heapq
    input = sys.stdin.readline

    n,m = map(int,input().split())
    a = tuple(map(int,input().split()))


    #Union Find
    par = [-1]*n
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


    for _ in [0]*m:
        x,y = map(int,input().split())
        unite(x,y)
    
    if m < (n-1)//2:
        print('Impossible')
        return
    
    h = [[] for _ in [0]*n]
    for i,e in enumerate(a):
        heapq.heappush(h[find(i)],e)
    
    root = []
    for i,e in enumerate(par):
        if e < 0:
            root.append(i)
    
    if len(root) == 1:
        print(0)
        return

    must = 0
    opt = []
    for i in root:
        must += heapq.heappop(h[i])
        for e in h[i]:
            opt.append(e)
    opt.sort()

    print(must+sum(opt[:len(root)-2]))



if __name__ =='__main__':
    main()