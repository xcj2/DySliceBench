def solve(H, W, grid):
    from collections import deque
    groups = [[0] * W for h in range(H)]
    v = 0 
    def search(M, h0, w0):
        nonlocal v
        count = [0, 0]
        Q = [(h0, w0)]
        groups[h0][w0] = M
        v+=1
        while Q:
            (h, w) = Q.pop()
            c = 1 - grid[h][w]
            count[1-c] += 1
            if h < H-1:
                if groups[h+1][w] == 0:
                    if grid[h+1][w] == c:
                        groups[h+1][w] = M
                        v += 1
                        Q.append((h+1, w))
                    else:
                        q.append((h+1, w))
            if h > 0:
                if groups[h-1][w] == 0:
                    if grid[h-1][w] == c:
                        groups[h-1][w] = M
                        v += 1
                        Q.append((h-1, w))
                    else:
                        q.append((h-1, w))
            if w > 0:
                if groups[h][w-1] == 0:
                    if grid[h][w-1] == c:
                        groups[h][w-1] = M
                        v += 1
                        Q.append((h, w-1))
                    else:
                        q.append((h, w-1))
            if w < W-1:
                if groups[h][w+1] == 0:
                    if grid[h][w+1] == c:
                        groups[h][w+1] = M
                        v += 1
                        Q.append((h, w+1))
                    else:
                        q.append((h, w+1))
        #print("search(%d,%d): %s"%(h0, w0, count))
        return count

    answer = 0
    m = 0
    q = deque()
    q.append((0,0))
    while q:
        h, w = q.pop()
        if groups[h][w] == 0:
            m+=1
            b, w = search(m, h, w)
            answer += b * w
    #for h in range(H): print(*groups[h])
    return answer

def main():
    import sys
    input = sys.stdin.readline
    H, W = map(int, input().split())

    grid = [[0]]*H
    for i in range(H):
        grid[i] = [1 if c == '#' else 0 for c in input().rstrip()]
    print(solve(H, W, grid))

main()


