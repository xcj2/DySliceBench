# D - Wizard in Maze
import sys
from collections import deque
from typing import List, Tuple


class WarpableMaze:
    __slots__ = ["height", "width", "road", "wall", "grid"]

    def __init__(
        self,
        height: int,
        width: int,
        grid: List[str],
        road: str = ".",
        wall: str = "#",
    ) -> None:
        # Values of start and goal must be 0-origin.
        self.height = height + 4
        self.width = width + 4
        self.road = road
        self.wall = wall
        self.grid = self._flatten_grid(grid)

    def _flatten_dxy(self, x: int, y: int) -> int:
        return self.width * x + y

    def _flatten_coordinate(self, h: int, w: int) -> int:
        return self._flatten_dxy(h + 2, w + 2)

    def _flatten_grid(self, grid: List[str]) -> str:
        flat_grid = self.wall * self.width * 2
        for row in grid:
            flat_grid += self.wall * 2 + row + self.wall * 2
        flat_grid += self.wall * self.width * 2
        return flat_grid

    def bfs(self, start_2d: Tuple[int, int], goal_2d: Tuple[int, int]) -> int:
        start = self._flatten_coordinate(*start_2d)
        goal = self._flatten_coordinate(*goal_2d)
        
        w = self.width
        move_to_warp = {
            -w: (-2 * w - 2, -2 * w - 1, -2 * w, -2 * w + 1, -w - 1),
            w: (w + 1, 2 * w - 1, 2 * w, 2 * w + 1, 2 * w + 2),
            -1: (-w - 2, -2, w - 2, w - 1, 2 * w - 2),
            1: (-w + 1, -2 * w + 2, -w + 2, 2, w + 2),
        }

        unsearched = 1 << 30
        dist = [unsearched] * (self.height * self.width)
        dist[start] = 0
        queue = deque([start])
        while queue:
            x = queue.popleft()
            cur_dist = dist[x]
            if x == goal:
                break

            for move, warp in move_to_warp.items():
                nx = x + move
                if self.grid[nx] == self.road:
                    if dist[nx] > cur_dist:
                        dist[nx] = cur_dist
                        queue.appendleft(nx)
                    continue

                for dx in warp:
                    nx = x + dx
                    if self.grid[nx] == self.wall:
                        continue
                    if dist[nx] > cur_dist + 1:
                        dist[nx] = cur_dist + 1
                        queue.append(nx)

        return dist[goal] if dist[goal] != unsearched else -1

    def debug(self):
        print("<DEBUG>", file=sys.stderr)
        for row in zip(*[iter(self.grid)] * self.width):
            print(*row, file=sys.stderr)


def main():
    H, W, CH, CW, DH, DW, *S = open(0).read().split()
    maze = WarpableMaze(int(H), int(W), S)
    start, goal = (int(CH) - 1, int(CW) - 1), (int(DH) - 1, int(DW) - 1)
    print(maze.bfs(start, goal))
    # maze.debug()


if __name__ == "__main__":
    main()
