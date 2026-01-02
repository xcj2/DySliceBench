# D - Wizard in Maze
import sys
from collections import deque
from typing import List, Tuple


class WarpableMaze:
    __slots__ = ["height", "width", "start", "goal", "road", "wall", "grid"]

    def __init__(
        self,
        height: int,
        width: int,
        start: Tuple[int, int],
        goal: Tuple[int, int],
        grid: List[str],
        road: str = ".",
        wall: str = "#",
    ) -> None:
        # Values of start and goal must be 0-origin.
        self.height = height + 4
        self.width = width + 4
        self.start = self._flatten_coordinate(*start)
        self.goal = self._flatten_coordinate(*goal)
        self.road = road
        self.wall = wall
        self.grid = self._flatten_grid(grid)

    def _flatten_coordinate(self, h: int, w: int) -> int:
        return self.width * (h + 2) + w + 2

    def _flatten_grid(self, grid: List[str]) -> str:
        flat_grid = self.wall * self.width * 2
        for row in grid:
            flat_grid += self.wall * 2 + row + self.wall * 2
        flat_grid += self.wall * self.width * 2
        return flat_grid

    def bfs(self) -> int:
        w = self.width
        move = (-w, w, -1, 1)
        warp = [-2 * w - 2, -2 * w - 1, -2 * w, -2 * w + 1, -2 * w + 2]
        warp.extend([-w - 2, -w - 1, -w + 1, -w + 2, -2, 2])
        warp.extend([w - 2, w - 1, w + 1, w + 2])
        warp.extend([2 * w - 2, 2 * w - 1, 2 * w, 2 * w + 1, 2 * w + 2])

        unsearched = -1
        dist = [unsearched] * (self.height * self.width)
        dist[self.start] = 0
        queue = deque([self.start])
        while queue:
            x = queue.popleft()
            if x == self.goal:
                break
            cur_dist = dist[x]

            for dx in move:
                nx = x + dx
                if self.grid[nx] == self.wall:
                    continue
                if dist[nx] == unsearched or dist[nx] > cur_dist:
                    dist[nx] = cur_dist
                    queue.appendleft(nx)

            for dx in warp:
                nx = x + dx
                if self.grid[nx] == self.wall:
                    continue
                if dist[nx] == unsearched or dist[nx] > cur_dist + 1:
                    dist[nx] = cur_dist + 1
                    queue.append(nx)

        return dist[self.goal]

    def debug(self):
        print(f"<DEBUG>\nstart={self.start}, goal={self.goal}", file=sys.stderr)
        for row in zip(*[iter(self.grid)] * self.width):
            print(*row, file=sys.stderr)


def main():
    H, W, CH, CW, DH, DW, *S = open(0).read().split()
    start, goal = (int(CH) - 1, int(CW) - 1), (int(DH) - 1, int(DW) - 1)
    maze = WarpableMaze(int(H), int(W), start, goal, S)
    # maze.debug()
    print(maze.bfs())


if __name__ == "__main__":
    main()
