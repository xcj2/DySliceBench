import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, K = LI()
    P = LI_()
    C = LI()

    ans = -INF
    for i in range(N):
        # iを含むサイクルの探索
        cycle = []
        c = i
        while True:
            c = P[c]
            cycle.append(c)
            if c == i:
                break
        len_cycle = len(cycle)
        # print(i, cycle, [C[j] for j in cycle])

        # 最大スコアの探索
        score = 0
        cycle_score_total = sum([C[j] for j in cycle])
        cycle_score_cum = list(itertools.accumulate([C[j] for j in cycle]))
        # 終了地点をjと決める
        for j in range(min(len_cycle, K)):
            score = cycle_score_cum[j]
            if cycle_score_total > 0:
                score += (K - j - 1) // len_cycle * cycle_score_total
            # print(j, score)
            ans = max(score, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
