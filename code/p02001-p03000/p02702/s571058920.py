import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
from collections import defaultdict
def main():
    S_ = S()
    mod_list = defaultdict(int)
    ans = 0
    num = 0
    point = 1
    for i in S_[::-1]:
        num += int(i) * point
        mod = int(num) % 2019
        mod_list[mod] += 1
        point *= 10
        point %= 2019
    values_ = mod_list.values()
    ans += mod_list[0]
    for value in values_:
        ans += (value - 1) * value // 2

    print(ans)

if __name__ == "__main__":
    main()
