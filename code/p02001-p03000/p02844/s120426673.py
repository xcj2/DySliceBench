import sys
from collections import defaultdict
import bisect
from itertools import product


sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]

def main():
    n = II()
    s = S()
    d = defaultdict(list)
    for i, c in enumerate(s):
        d[int(c)].append(i)

    strs = [i for i in range(10)]
    lens = [len(d[i]) for i in strs]
    ans = 0

    for i, j, k in product(strs, strs, strs):
        if lens[i] == 0 or lens[j] == 0 or lens[k] == 0:
            continue
        index_i = 0
        index_j = bisect.bisect_right(d[j], d[i][index_i])
        if index_j == lens[j]:
            continue
        index_k = bisect.bisect_right(d[k], d[j][index_j])
        if index_k == lens[k]:
            continue
        ans += 1
    print(ans)




if __name__ == '__main__':
    main()