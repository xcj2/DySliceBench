"""
Maze class.

cf. WarpableMaze class.
"""
import sys
from collections import deque
from typing import List, Tuple


class Maze:
    __slots__ = [
        "height",
        "width",
        "road",
        "wall",
        "is_unsearched",
        "is_unreachable",
        "dist",
    ]

    def __init__(
        self,
        height: int,
        width: int,
        grid: List[bytes],
        *,
        road: str = ".",
        wall: str = "#",
        is_unsearched: int = 1 << 30,
        is_unreachable: int = -1,
    ) -> None:
        self.height = height + 2
        self.width = width + 2
        self.road = road
        self.wall = wall
        self.is_unsearched = is_unsearched
        self.is_unreachable = is_unreachable
        self.dist = self._convert_grid_to_dist(grid)

    def _convert_grid_to_dist(self, grid: List[bytes]) -> List[int]:
        """Convert a 2D grid to a 1D dist."""
        dist = [self.is_unreachable] * self.height * self.width
        i = self.width
        for row in grid:
            for c in row.decode():
                i += 1
                if c == self.road:
                    dist[i] = self.is_unsearched
            i += 2
        return dist

    def _flatten_coordinate(self, x: int, y: int) -> int:
        """Flatten 2D coordinate values.
        Values of a coordinate must be 1-origin.
        """
        return self.width * x + y

    def bfs(
        self,
        start_2d: Tuple[int, int],
        goal_2d: Tuple[int, int],
        updates_dist: bool = False,
    ) -> int:
        """BFS to compute the distance from start to goal.
        Values of start_2d and goal_2d must be 1-origin.
        """
        start = self._flatten_coordinate(*start_2d)
        goal = self._flatten_coordinate(*goal_2d)

        moves = (-self.width, self.width, -1, 1)
        dist = self.dist[:]
        dist[start] = 0
        queue = deque([start])

        while queue:
            x = queue.popleft()
            cur_dist = dist[x]
            if x == goal:
                break

            for dx in moves:
                nx = x + dx
                if dist[nx] == self.is_unsearched:
                    dist[nx] = cur_dist + 1
                    queue.append(nx)

        if updates_dist:
            self.dist = dist
        return dist[goal] if dist[goal] != self.is_unsearched else self.is_unreachable

    def debug(self) -> None:
        """Show debugging information."""
        print(
            f"<DEBUG>\n"
            f"height={self.height}, width={self.width}\n"
            f"is_unsearched={self.is_unsearched}, is_unreachable={self.is_unreachable}",
            file=sys.stderr,
        )

        convert = lambda x: self.road if x != self.is_unreachable else self.wall
        for row in zip(*[iter(self.dist)] * self.width):
            print(*map(convert, row), file=sys.stderr)


def abc007_c():
    # https://atcoder.jp/contests/abc007/tasks/abc007_3
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline

    R, C = map(int, readline().split())
    (*start,) = map(int, readline().split())
    (*goal,) = map(int, readline().split())
    (*S,) = read().split()

    maze = Maze(R, C, S)
    print(maze.bfs(start, goal))


def abc088_d():
    # https://atcoder.jp/contests/abc088/tasks/abc088_d
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline

    H, W = map(int, readline().split())
    (*S,) = read().split()
    maze = Maze(H, W, S)

    dist = maze.bfs((1, 1), (H, W))
    if dist != -1:
        res = H * W - sum((row.decode()).count("#") for row in S) - dist - 1
        print(res)
    else:
        print(-1)


if __name__ == "__main__":
    # abc007_c()
    abc088_d()
