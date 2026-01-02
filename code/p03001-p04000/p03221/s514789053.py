import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

def ume(x):
    x = str(x)
    if len(x) < 6:
        return '0'*(6-len(x)) + x
    return x

def main():
    N, M = mi()

    l = dp2(0, 3, M)
    cnt = [0]*(N+1)
    ans = dp2(0, 2, M)
    for i in range(M):
        p, y = mi()
        l[i][0], l[i][1], l[i][2] = p-1, y, i
        cnt[p] += 1
    for i in range(N):
        cnt[i+1] += cnt[i]

    l.sort(key=lambda x: x[0])
    for i in range(N):
        ichibu = l[cnt[i]:cnt[i+1]]
        ichibu.sort(key=lambda x: x[1])
        for j in range(cnt[i+1]-cnt[i]):
            ans[ichibu[j][2]][0] =ichibu[j][0]+1
            ans[ichibu[j][2]][1] =j+1
    
    for x, y in ans:
        print(ume(x)+ume(y))


if __name__ == "__main__":
    main()