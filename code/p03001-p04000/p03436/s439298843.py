def read():
    H, W = map(int, input().split(' '))
    Ss = []
    for _ in range(H):
        Ss.append(input())
    return H, W, Ss
 
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
 
def add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])
 
def ans(H, W, Ss):
    if Ss[0][0] == '#':
        print('0,0 #')
        return -1
    ds =[ [-1 for _ in range(W)] for _ in range(H)]
    ds[0][0] = 1
    q = [(0, 0)]
    while q:
        p = q.pop()
        d = ds[p[1]][p[0]]
        for dr in DIRS:
            x, y = add(p, dr)
            if x < 0 or x >= W or y < 0 or y >= H:
                continue # 範囲外へは移動できない
            if Ss[y][x] == '#':
                continue # 行き止まりへは移動できない
            if ds[y][x] >= 0 and ds[y][x] <= d + 1: # すでに訪れていて短縮にもなっていない
                continue
            ds[y][x] = d + 1
            q.append((x, y))
    if ds[H-1][W-1] < 0:
        return -1
    # 白マスを数える
    ws = sum([l.count('.') for l in Ss])
    return ws - ds[H-1][W-1]
 
if __name__ == '__main__':
    H, W, Ss = read()
    print(ans(H, W, Ss))