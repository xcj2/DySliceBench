import sys
# input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import math
import heapq
from collections import defaultdict, Counter, deque
from bisect import bisect_left
MOD = 10**9 + 7
INF = 1 << 20


def main():
    n = getN()
    s = input().strip()

    rs = []
    gs = []
    bs = []
    for i, c in enumerate(s):
        if c == "R":
            rs.append(i)
        elif c == "G":
            gs.append(i)
        else:
            bs.append(i)


    lr, lg, lb = len(rs), len(gs), len(bs)
    ans = 0
    # print(s, s[1])
    tgt = {"R": rs, "G":gs, "B": bs }
    idxs = {"R": lr, "G": lg, "B": lb}
    for i in range(n-1):
        first = s[i]
        for j in range(i+1, n):
            # first = s[i]
            second = s[j]
            # print(i, j)
            if first == second:
                continue
            else:
                # print(first, second)
                rem = ["R", "G", "B"]
                rem.remove(first)
                rem.remove(second)
                remm = rem[0]
                # print(i, j, remm)
                ans += idxs[remm] - bisect_left(tgt[remm], j)
                if (2*j - i) < n and s[2*j - i] == remm:
                    ans -= 1
                    # print("substracted")
    print(ans)

if __name__ == '__main__':
    main()
