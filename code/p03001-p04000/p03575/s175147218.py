'''
ABC 075
https://www.youtube.com/watch?v=VJntQuR2zNI

'''
def inpl(): return input().split()
def arr(r, c): return [[False for x in range(c)] for y in range(r)]

def dfs(x):
    if vis[x]:
        return
    else:
        vis[x] = True
        for i in range(n):
            if graph[x][i]:
                dfs(i)

if __name__ == '__main__':
    n, m = map(int, inpl())
    M = [list(map(int, inpl())) for _ in range(m)]

    ans = 0
    for e in range(m):#e:取り除く辺    
        graph = arr(n, n)#arr(i, j): i, j間に辺があればTrue
        for i in range(m):
            if i == e:
                continue
            a, b = M[i]
            #inputは1インデックス
            #graphは0インデックスなので、1減
            graph[a - 1][b - 1] = True
            graph[b - 1][a - 1] = True

        vis = [False for _ in range(n)]#訪れていたらTrue
        dfs(0)#0から辿れる範囲をvis = Trueにする
        
        connected = True
        for i in range(n):
            if not vis[i]:
                connected = False
                break
        if not connected:
            ans += 1
    print(ans)