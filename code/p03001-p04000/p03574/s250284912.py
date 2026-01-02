def makelist(n, m):
    return [[0 for i in range(m)] for j in range(n)]


H, W = map(int, input().split())
S = [0]*H
for i in range(H):
    S[i] = input()

ans = makelist(H, W)

def check(p):
    x, y = p
    return x >= 0 and y >= 0 and x < W and y < H

def calc(p, vol):
    return (p[0]+vol[0], p[1]+vol[1])

vols = [ (x, y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0] 

for y in range(H):
    for x in range(W):
        if S[y][x] == '#':
            ans[y][x] = '#'
            for vol in vols:
                now = calc((x, y), vol)
                if check(now):
                    if ans[now[1]][now[0]] != '#':
                        ans[now[1]][now[0]] += 1
for e in ans:
    print("".join(map(str, e)))
