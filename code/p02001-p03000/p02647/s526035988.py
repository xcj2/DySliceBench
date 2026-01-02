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


def solveFast(values: List[int], N: int, K: int) -> List[int]:
    result = [0] * N
    for v, i in sorted(((v, i) for i, v in enumerate(values)), reverse=True):
        v = max(v, K)
        for j in range(max(0, i - v), min(N, v + i + 1)):
            n = abs(j - i)
            if n == 0:
                result[j] += 1
            else:
                result[j] += n * (n + 1) // 2
    return result


def solve(values: List[int], N: int, K: int) -> List[int]:
    if K >= N - 1:
        return [N] * N
    for _k in range(K):
        prev = values.copy()
        values = [0] * N
        for i, v in enumerate(prev):
            l = max(0, i - v)
            r = min(N - 1, v + i)
            values[l] += 1
            if r < N - 1:
                values[r + 1] -= 1
        for i in range(1, N):
            values[i] += values[i - 1]
        if all(v == N for v in values):
            break
    return values


def do_job(stdin, stdout):
    "Do the work"
    LOG.debug("Start working")
    # first line is number of test cases
    N, K = map(int, stdin.readline().split())
    values = list(map(int, stdin.readline().split()))
    # values = []
    # for _ in range(N):
    #     values.append(stdin.readline().split())
    result = solve(values, N, K)
    print(*result, file=stdout)


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
