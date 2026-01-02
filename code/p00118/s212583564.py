import sys
sys.setrecursionlimit(10 ** 8)

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():

    for _ in range(22):
        h, w = ZZ()
        if h == 0 and w == 0: break
        A = [input() for _ in range(h)]
        D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        done = [[False] * w for _ in range(h)]
        ans = 0

        def dfs(x, y, fluit):
            if done[x][y]: return
            done[x][y] = True
            for dx, dy in D:
                nx, ny = x+dx, y+dy
                if 0 <= nx < h and 0 <= ny < w and A[nx][ny] == fluit: dfs(nx, ny, fluit)

        ans = 0
        for i in range(h):
            for j in range(w):
                if done[i][j]: continue
                ans += 1
                dfs(i, j, A[i][j])
        print(ans)

    return

if __name__ == '__main__':
    main()

