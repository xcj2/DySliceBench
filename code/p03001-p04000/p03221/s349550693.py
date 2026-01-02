import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

def main():
    N, M = mi()
    l = dp2(0, 3, M)
    for i in range(M):
        p, x = mi()
        l[i][0], l[i][1], l[i][2] = p, x, i 
    l.sort(key=lambda x :(x[0], x[1]))

    ans = ['' for _ in range(M)]
    cnt = 0
    bf = 1
    for i in range(M):
        a = l[i][0]
        if a > bf:
            cnt = i
        b, c = str(i+1-cnt), l[i][2]
        ans[c] = str(a).zfill(6) + b.zfill(6)
        bf = a

    
    for a in ans:
        print(a)

if __name__ == "__main__":
    main()