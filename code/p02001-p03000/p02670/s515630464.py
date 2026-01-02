#!/usr/bin/env python3
# vim: set fileencoding=utf-8

# pylint: disable=unused-import, invalid-name, missing-docstring, bad-continuation


"""Module docstring
"""

import functools
import heapq
import itertools
import logging
import math
import os
import random
import string
import sys
from argparse import ArgumentParser
from collections import defaultdict, deque
from copy import deepcopy
from io import BytesIO, IOBase
from typing import Dict, List, Optional, Set, Tuple

# sys.setrecursionlimit(pow(2, 31) - 1)

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


def solve(values: List[int], nb: int) -> int:
    # min nb of neighbours from here to exit
    grid = [[min(i, nb - i - 1, j, nb - j - 1) for j in range(nb)] for i in range(nb)]
    answer = 0
    still_inside = [[True] * nb for _ in range(nb)]
    # LOG.debug(("\n".join(map(str, grid))))
    for v in values:
        i, j = divmod(v - 1, nb)
        answer += grid[i][j]
        # LOG.debug((i, j, grid[i][j]))
        still_inside[i][j] = False
        dfs(nb, grid, i, j, still_inside)
        # LOG.debug(("\n".join(map(str, grid))))
    return answer


def dfs(
    nb: int,
    grid: List[List[int]],
    removed_i: int,
    removed_j: int,
    still_inside: List[List[bool]],
):
    q = deque([(removed_i, removed_j, grid[removed_i][removed_j])])
    while q:
        i, j, cur_cost = q.pop()
        if i > 0 and grid[i - 1][j] > cur_cost:
            grid[i - 1][j] = cur_cost
            q.append((i - 1, j, cur_cost + still_inside[i - 1][j]))
        if j > 0 and grid[i][j - 1] > cur_cost:
            grid[i][j - 1] = cur_cost
            q.append((i, j - 1, cur_cost + still_inside[i][j - 1]))
        if i < nb - 1 and grid[i + 1][j] > cur_cost:
            grid[i + 1][j] = cur_cost
            q.append((i + 1, j, cur_cost + still_inside[i + 1][j]))
        if j < nb - 1 and grid[i][j + 1] > cur_cost:
            grid[i][j + 1] = cur_cost
            q.append((i, j + 1, cur_cost + still_inside[i][j + 1]))


def update_neighbours(nb: int, grid: List[List[int]], i: int, j: int):
    # update neighbours
    if j < nb - 1:
        grid[i][j][RIGHT] = grid[i][j + 1][RIGHT]
    if j > 0:
        grid[i][j][LEFT] = grid[i][j - 1][LEFT]
    if i < nb - 1:
        grid[i][j][UP] = grid[i + 1][j][UP]
    if i > 0:
        grid[i][j][DOWN] = grid[i - 1][j][DOWN]
    for left in range(j):
        grid[i][left][RIGHT] = max(0, grid[i][left][RIGHT])
    for right in range(j + 1, nb):
        grid[i][right][LEFT] = max(0, grid[i][right][LEFT])
    for up in range(i):
        grid[up][j][DOWN] = max(0, grid[up][j][DOWN])
    for down in range(i + 1, nb):
        grid[down][j][UP] = max(0, grid[down][j][UP])


def do_job(stdin, stdout):
    "Do the work"
    LOG.debug("Start working")
    # first line is number of test cases
    N = int(stdin.readline().strip())
    values = list(map(int, stdin.readline().split()))
    # values = []
    # for _ in range(N):
    #     values.append(stdin.readline().split())
    result = solve(values, N)
    print(result, file=stdout)


def print_output(testcase: int, result, stdout) -> None:
    "Formats and print result"
    if result is None:
        result = "IMPOSSIBLE"
    print("Case #{}: {}".format(testcase + 1, result), file=stdout)
    # 6 digits float precision {:.6f} (6 is the default value)
    # print("Case #{}: {:f}".format(testcase + 1, result), file=stdout)


BUFSIZE = 8192


class FastIO(IOBase):
    # pylint: disable=super-init-not-called, expression-not-assigned
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    # pylint: disable=super-init-not-called
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


def configure_log() -> None:
    "Configure the log output"
    log_formatter = logging.Formatter("L%(lineno)d - " "%(message)s")
    handler = logging.StreamHandler(IOWrapper(sys.stderr))
    handler.setFormatter(log_formatter)
    LOG.addHandler(handler)


LOG = None
# for interactive call: do not add multiple times the handler
if not LOG:
    LOG = logging.getLogger("template")
    configure_log()


def main(argv=None):
    "Program wrapper."
    if argv is None:
        argv = sys.argv[1:]
    parser = ArgumentParser()
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        default=False,
        help="run as verbose mode",
    )
    args = parser.parse_args(argv)
    if args.verbose:
        LOG.setLevel(logging.DEBUG)
    stdin = IOWrapper(sys.stdin)
    stdout = IOWrapper(sys.stdout)
    do_job(stdin, stdout)
    stdout.flush()
    for h in LOG.handlers:
        h.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
