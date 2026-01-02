#!/usr/bin/env python3
from collections import deque
import sys
try:
    from typing import Deque, Dict, List, Tuple
except ImportError:
    pass


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, M: int, L: "List[int]", R: "List[int]", D: "List[int]"):
    G = [[] for _ in range(N)]  # type: List[List[Tuple[int, int]]]
    for Li, Ri, Di in zip(L, R, D):
        Li -= 1
        Ri -= 1
        G[Li].append((Ri, Di))
        G[Ri].append((Li, -Di))
    pos = {}  # type: Dict[int, int]
    for i in range(N):
        if i in pos:
            continue
        q = deque()  # type: Deque[int]
        pos[i] = 0
        q.append(i)
        while q:
            s = q.popleft()
            for t, dst in G[s]:
                if t in pos:
                    if pos[t] != pos[s] + dst:
                        print(NO)
                        return
                    continue
                pos[t] = pos[s] + dst
                q.append(t)
    print(YES)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    L = [int()] * (M)  # type: "List[int]"
    R = [int()] * (M)  # type: "List[int]"
    D = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, M, L, R, D)


if __name__ == '__main__':
    main()
