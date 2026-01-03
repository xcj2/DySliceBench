import sys
input = sys.stdin.readline

def main():
    N = int(input())
    rx,ry = [],[]
    _root = []
    for i in range(N):
        a,b = map(int,input().split())
        rx.append((a,i))
        ry.append((b,i))
    
    I = [i for i in range(N)]
    rank = [1 for _ in range(N)]
    def root(x):
        if x == I[x]:
            return x
        I[x] = root(I[x])
        return I[x]
    
    def unite(x,y):
        px,py = root(x),root(y)
        rx,ry = rank[px],rank[py]
        if rx > ry:
            I[py] = px
        else:
            I[px] = py
            if rx == ry:
                rank[py] += 1

    ans = 0
    rx.sort()
    ry.sort()
    for i in range(N-1):
        dx = rx[i+1][0]-rx[i][0]
        dy = ry[i+1][0]-ry[i][0]
        _root.append((dx,rx[i][1],rx[i+1][1]))
        _root.append((dy,ry[i][1],ry[i+1][1]))
        
    _root.sort()
    a = len(_root)
    for i in range(a):
        cost,now,fol = _root[i]
        if (root(now) == root(fol)):
            continue
        ans += cost
        unite(now,fol)
        
    print(ans)
    
if __name__ == "__main__":
    main()