def main():
    H, W = map(int, input().split())
    S = []
    max_move = 0
    for _ in range(H):
        S.append(list(input()))

    for hs in range(H):
        for ws in range(W):
            if S[hs][ws] == '#':
                continue
            answer = bfs(S, H, W, hs, ws)
            if max_move < answer:
                max_move = answer
    print(max_move)

def bfs(S, H, W, hs, ws):
    visited = [[-1] * W for _ in range(H)]
    s = (hs, ws, 0)
    queue = [s]
    c = s
    max_c = 0
    while len(queue) > 0:
        c = queue.pop(0)
        count = c[2]
        if count > max_c:
            max_c = count
        # 確認済みに追加
        visited[c[0]][c[1]] = 1
        # 上
        enqueue(c[0] - 1, c[1], S, H, W, queue, count, visited)
        # 左
        enqueue(c[0], c[1] - 1, S, H, W, queue, count, visited)
        # 下
        enqueue(c[0] + 1, c[1], S, H, W, queue, count, visited)
        # 右
        enqueue(c[0], c[1] + 1, S, H, W, queue, count, visited)
    # 最短距離を返す
    return max_c

def enqueue(i, j, S, H, W, queue, count, visited):
    if i >= 0 and i < H and j >= 0 and j < W and visited[i][j] == -1 and S[i][j] == '.':
        queue.append((i, j, count + 1))
        visited[i][j] = 1

main()
