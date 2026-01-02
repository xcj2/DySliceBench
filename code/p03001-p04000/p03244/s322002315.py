#!/usr/bin/env python3
from collections import Counter
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(n: int, v: "List[int]"):
    v1 = v[::2]
    v2 = v[1::2]
    c1 = Counter(v1)
    c2 = Counter(v2)
    mc1 = c1.most_common(2)
    mc2 = c2.most_common(2)
    if len(mc1) == 1:
        mc1.append((999990, 0))
    if len(mc2) == 1:
        mc2.append((999999, 0))
    cv1, cnt1 = mc1[0]
    cv2, cnt2 = mc2[0]
    if cv1 != cv2:
        print(n - cnt1 - cnt2)
    else:
        print(n - max(cnt1 + mc2[1][1], cnt2 + mc1[1][1]))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    v = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    solve(n, v)


if __name__ == '__main__':
    main()
