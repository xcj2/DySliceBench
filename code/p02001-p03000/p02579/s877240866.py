# D - Wizard in Maze
import sys
from collections import deque
from typing import List, Tuple


class WarpableMaze:
    __slots__ = ["height", "width", "road", "wall", "unsearched", "dist"]

    def __init__(
        self,
        height: int,
        width: int,
        grid: List[bytes],
        road: str = ".",
        wall: str = "#",
    ) -> None:
        self.height = height + 4
        self.width = width + 4
        self.road = road
        self.wall = wall
        self.unsearched = 1 << 30
        self.dist = self._convert_grid_to_dist(grid)

    def _flatten_dxy(self, x: int, y: int) -> int:
        return self.width * x + y

    def _flatten_coordinate(self, h: int, w: int) -> int:
        return self._flatten_dxy(h + 2, w + 2)

    def _convert_grid_to_dist(self, grid: List[bytes]) -> List[int]:
        dist = [-1] * self.height * self.width
        i = self.width * 2 + 1
        for row in grid:
            for c in row.decode():
                i += 1
                if c == self.road:
                    dist[i] = self.unsearched
            i += 4
        return dist

    def bfs(self, start_2d: Tuple[int, int], goal_2d: Tuple[int, int]) -> int:
        start = self._flatten_coordinate(*start_2d)
        goal = self._flatten_coordinate(*goal_2d)

        w = self.width
        walk_to_warp = {
            -w: (-2 * w - 2, -2 * w - 1, -2 * w, -2 * w + 1, -w - 1),
            w: (w + 1, 2 * w - 1, 2 * w, 2 * w + 1, 2 * w + 2),
            -1: (-w - 2, -2, w - 2, w - 1, 2 * w - 2),
            1: (-w + 1, -2 * w + 2, -w + 2, 2, w + 2),
        }

        dist = self.dist[:]
        dist[start] = 0
        queue = deque([start])
        while queue:
            next_queue = deque()
            while queue:
                x = queue.popleft()
                cur_dist = dist[x]
                if x == goal:
                    break
    
                for walk, warp in walk_to_warp.items():
                    nx = x + walk
                    if dist[nx] > cur_dist:
                        dist[nx] = cur_dist
                        queue.append(nx)
                        continue
                    if dist[nx] >= 0:
                        continue
    
                    for dx in warp:
                        nx = x + dx
                        if dist[nx] > cur_dist + 1:
                            dist[nx] = cur_dist + 1
                            next_queue.append(nx)
            queue = next_queue

        return dist[goal] if dist[goal] != self.unsearched else -1


def main():
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline

    H, W = map(int, readline().split())
    CH, CW = map(int, readline().split())
    DH, DW = map(int, readline().split())
    (*S,) = read().split()

    maze = WarpableMaze(H, W, S)
    start, goal = (CH - 1, CW - 1), (DH - 1, DW - 1)
    print(maze.bfs(start, goal))


if __name__ == "__main__":
    main()
