# D - Wizard in Maze
import sys
from collections import deque
from typing import List, Tuple


class WarpableMaze:
    __slots__ = ["height", "width", "road", "wall", "unsearched", "grid"]

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
        self.grid = self._flatten_grid(grid)

    def _flatten_dxy(self, x: int, y: int) -> int:
        return self.width * x + y

    def _flatten_coordinate(self, h: int, w: int) -> int:
        return self._flatten_dxy(h + 2, w + 2)

    def _flatten_grid(self, grid: List[bytes]) -> str:
        flat_grid = self.wall * (self.width * 2)
        for row in grid:
            flat_grid += self.wall * 2 + row.decode() + self.wall * 2
        flat_grid += self.wall * (self.width * 2)
        return flat_grid

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

        convert = lambda c: self.unsearched if c == self.road else -1
        dist = list(map(convert, self.grid))
        dist[start] = 0
        queue = deque([start])
        while queue:
            x = queue.popleft()
            cur_dist = dist[x]
            if x == goal:
                break

            for walk, warp in walk_to_warp.items():
                nx = x + walk
                if dist[nx] > cur_dist:
                    dist[nx] = cur_dist
                    queue.appendleft(nx)
                    continue
                if dist[nx] >= 0:
                    continue

                for dx in warp:
                    nx = x + dx
                    if dist[nx] > cur_dist + 1:
                        dist[nx] = cur_dist + 1
                        queue.append(nx)

        return dist[goal] if dist[goal] != self.unsearched else -1

    def debug(self):
        print("<DEBUG>", file=sys.stderr)
        for row in zip(*[iter(self.grid)] * self.width):
            print(*row, file=sys.stderr)


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
    # maze.debug()


if __name__ == "__main__":
    main()
