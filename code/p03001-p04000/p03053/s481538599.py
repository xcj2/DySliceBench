# import sys
# input = sys.stdin.readline
import collections

def main():
    H, W = input_list()
    grid = [input() for i in range(H)]
    dist = [[-1]*W for _ in range(H)]
    black_cells = collections.deque()
    for h in range(H):
        for w in range(W):
            if grid[h][w] == '#':
                black_cells.append((h, w))
                dist[h][w] = 0

    def bfs(black_cells, dist):
        d = 0
        while black_cells:
            h, w = black_cells.popleft()
            d = dist[h][w]
            for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                new_h = h + dy
                new_w = w + dx
                if new_h < 0 or H <= new_h or new_w < 0 or W <= new_w:
                    continue
                if dist[new_h][new_w] == -1:
                    dist[new_h][new_w] = d + 1
                    black_cells.append((new_h, new_w))
        return d
    
    print(bfs(black_cells, dist))
    
#6 5 2 5 3 2
#1 2 3 4 5 6

def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
