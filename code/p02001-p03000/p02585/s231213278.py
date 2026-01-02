import sys, math
from functools import lru_cache
from collections import defaultdict
sys.setrecursionlimit(500000)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def main():
    N, K = mi()
    P = list(mi())
    C = list(mi())

    # loopを格納
    loops = []
    # 数えたかどうか
    done = [False]*N
    
    for i in range(N):
        # もう数えているならskip
        if done[i]:
            continue

        now = P[i]-1
        T = 1
        s = C[now]
        lst = [now]

        done[now] = True

        # 戻ってくるまでループ
        while now != i:
            now = P[now]-1
            T += 1
            s += C[now]
            lst.append(now)

            done[now] = True

        loops.append((T, s, lst))

    # print(loops)

    ans = -math.inf

    # 各loopごと
    for loop in loops:
        # loopの周期、総和、構成要素を取得
        T, s, lst = loop

        if s <= 0:
            m = -math.inf
            for v in lst:
                now = v
                ss = 0
                for _ in range(min(K, T)):
                    now = P[now]-1
                    ss += C[now]
                    m = max(m, ss)

            ans = max(ans, m)

        else:
            n = max(K//T-1, 0)
            rest = K-n*T
            m = -math.inf

            for v in lst:
                now = v
                ss = 0
                for _ in range(rest):
                    now = P[now]-1
                    ss += C[now]
                    m = max(m, ss)
            
            ans = max(ans, m+n*s)
    print(ans)



if __name__ == '__main__':
    main()