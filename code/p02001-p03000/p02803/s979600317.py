import queue


class Solution:

    def solve(self, H: int, W: int, S) -> int:

        def onEdge(pos):
            i = pos[0]
            j = pos[1]
            if 0 < i and i < H - 1 and 0 < j and j < W - 1:
                return False
            else:
                return True

        def bfs(start):
            INF = H*W+1
            dist = {}
            for i in range(H):
                for j in range(W):
                    dist[(i, j)] = INF

            max_dist = 0

            dist[start] = 0
            nexts = queue.Queue()
            nexts.put(start)

            while not nexts.empty():
                __next = nexts.get()

                # if onEdge(__next):
                max_dist = max(dist[__next], max_dist)

                for delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    h = __next[0] + delta[0]
                    w = __next[1] + delta[1]

                    if h < 0 or h > H - 1 or w < 0 or w > W - 1:
                        continue

                    if S[h][w] != "#":
                        if dist[(h, w)] == INF:
                            nexts.put((h, w))
                            dist[(h, w)] = dist[__next] + 1

            return max_dist

        ans = 0
        for i in range(H):
            for j in range(W):

                # skip if (i,j) is not on the edge
                # if not onEdge((i, j)):
                #     continue

                # skip if (i,J) is a wall
                if S[i][j] == "#":
                    continue

                ans = max(bfs((i, j)), ans)

        return ans


if __name__ == '__main__':

    # standard input
    H, W = map(int, input().split())
    S = []
    for h in range(H):
        S.append(input())

    # solve
    solution = Solution()
    print(solution.solve(H, W, S))
