from sys import stdin, stdout
def readLine_int_list():return list(map(int, stdin.readline().split()))

def is_biparate(links):
    '''
    0=white,1=blackとする
    2部グラフなら黒に塗られている頂点の数を返す
    2部グラフでないなら-1を返す。
    '''
    
    colors = [-1] * n
    colors[0] = 0
    q = [(0, 0)]  #0=white, 1=blackとする
    visited = set()
    while q:
        v, c = q.pop()
        if v in visited:
            if colors[v] != c: #最初に塗られた色とは反対の色が塗られるなら
                return -1
            continue
        visited.add(v)
        colors[v] = c
        for u in links[v]:
            q.append((u, c ^ 1))  #0^0=1 1^1=0 vとは反対の色を塗る
    return sum(colors)  #1の数 = blackの数
 




n, m = readLine_int_list()
g = [set() for _ in range(n)]

def main():
    for _ in range(m):
        a, b = readLine_int_list()
        a -= 1
        b -= 1
        g[a].add(b)
        g[b].add(a)
    
    
    
    bp1 = is_biparate(g)
    if bp1 == -1:
        '''
        2部グラフではない場合
            結論：完全グラフになるまで辺を追加できる
            →why
                奇サイクル上のある点をvとする
                s → v → tが偶数長でも、 奇サイクルの他の頂点を余計に経由することで奇数長になる
                s → tが奇数長になれば線が引ける
                つまり、任意の頂点間において奇数長が存在することになる
            完全グラフの辺の数は、n * (n - 1) // 2
            これには元あった辺の数まで含まれているので、 -m する
        '''
        max_m = n * (n - 1) // 2
    else:
        '''
        2部グラフの場合
            結論:(blackの数*whiteの数)本、線ができる
            why
                奇数閉路が存在しない => 異なる色間は必ず奇数長、同色間は必ず偶数長 
                1. whiteとblackの間は奇数長のパスが存在する ->線が引ける
                2. 同じ色どうしには奇数長のパスは存在しない -> 線は引かれない
                black=3, white=2の時の線の引き方 = b*w
            b*wにはパスの長さが1つまりもともとのパスが含まれてるので、-m　する
        '''
        max_m = bp1 * (n - bp1)
        
    print(max_m - m)
    

if __name__ == "__main__":
    main()