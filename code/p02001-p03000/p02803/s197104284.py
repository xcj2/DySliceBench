dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def get_child(M, i, j, h, w, vis):
    child = []
    for k in range(4):
        x = i + dr[k]
        y = j + dc[k]
        if 0<= x< h and 0 <= y < w and (x, y) not in vis and M[x][y]!='#':
            child.append((x, y))

    return child

def bfs(M, i, j, h, w):
    vis = {(i, j): True}
    li = [(i, j, 0)]
    mx = 0
    while li:
        tp = li.pop(0)
        mx = max(mx, tp[2])
        ch = get_child(M, tp[0], tp[1], h, w, vis)
        vis.update( {}.fromkeys(ch, True) )
        
        ch = [(t[0], t[1], tp[2]+1) for t in ch]
        li.extend(ch)

    return mx
        
        
def solve(M, h, w):
    ans = 0
    for r in range(h):
        for c in range(w):
            if M[r][c]=='.':
                ## start bfs from this point
                depth = bfs(M, r, c, h, w)
                ans = max(ans, depth)
    print(ans)
h, w = map(int, input().split())
Mat = []
for row in range(h):
    Mat.append(input())


solve(Mat, h, w)
