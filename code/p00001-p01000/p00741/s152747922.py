import sys
sys.setrecursionlimit(10000)

def place(i, j, w):
    return i*w + j

def get_path(w, h, c):
    path = list()
    for i in range(h):
        for j in range(w):
            # place = i*w + j
            can_go = list()
            if c[i][j] != 0:
                if i != 0 and c[i-1][j] != 0:
                    can_go.append( place(i-1, j, w) )
                
                if i != h-1 and c[i+1][j] != 0:
                    can_go.append( place(i+1, j, w) )

                if j != 0 and c[i][j-1] != 0:
                    can_go.append( place(i, j-1, w) )
                
                if j != w-1 and c[i][j+1] != 0:
                    can_go.append( place(i, j+1, w) )
                
                if i != 0 and j!= 0 and c[i-1][j-1] != 0:
                    can_go.append( place(i-1, j-1, w) )
                
                if i != 0 and j != w-1 and c[i-1][j+1] != 0:
                    can_go.append( place(i-1, j+1, w) )
                
                if i!= h-1 and j != 0 and c[i+1][j-1] != 0:
                    can_go.append( place(i+1, j-1, w) )
                
                if i!= h-1 and j != w-1 and c[i+1][j+1] != 0:
                    can_go.append( place(i+1, j+1, w) )
                
            path.append(can_go)
    
    return path

def dfs(p, path, visit, w, h, c):
    visit[p] = 1 # 来訪時刻の記録

    for nxt in path[p]: #繋がってる点の内
        if visit[nxt] == 0: # 未探索の場合には
            dfs(nxt, path, visit, w, h, c) # 先に進む
    
    return

# def print_path(i, j, path, w, h):
#     arr = path[i*w + j]
#     print("print path start")
#     for x in arr:
#         print(x//w, x%w)
#     print("print path fin")

def solve(w, h, c):
    path = get_path(w, h, c)
    visit = [0]*(w*h)

    # print_path(3, 18, path, w, h)
    ans = 0
    for place in range(w*h):
        i = place // w
        j = place % w
        if c[i][j] != 0 and visit[place] == 0:
            dfs(place, path, visit, w, h, c)
            # print(i, j)
            ans += 1
    
    print(ans)
    return 

w, h = map(int, input().split())
while w != 0 and h != 0:
    c = [list(map(int, input().split())) for _ in range(h)]
    solve(w, h, c)
    w, h = map(int, input().split())
