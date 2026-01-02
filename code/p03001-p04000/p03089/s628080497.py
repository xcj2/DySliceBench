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

def main():
    N = ii()
    B = li()

    '''
    flag = [0]*N
    l = N
    i = ind = N-1
    while True:
        if S[ind] == i:
            flag[ind] = 0

        while flag[i]:
            i -= 1
        ind = i
    '''
    ans = []
    for i in range(N):
        flag = 1
        for j in reversed(range(N-i)):
            if B[j] == j+1:
                a = B.pop(j)
                ans.append(a)
                flag = 0
                break
        if flag:
            print('-1')
            exit()

    for i in reversed(range(N)):
        print(ans[i])

if __name__ == "__main__":
    main()