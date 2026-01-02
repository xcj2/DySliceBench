import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N, K = LI()
    P = LI_()
    C = LI()
    G = [-1 for _ in range(N)]
    for i, p in enumerate(P):
        G[i] = p
    seen = set()

    loop_score = []
    loop_size = []
    loop_id2node = collections.defaultdict(list)

    _id = 0
    def calc_one_loop(v):
        nodes = set()
        if G[v] == -1:
            return -1, -1
        # calc loop, and return score
        score = 0
        size = 0
        while G[v] not in seen:
            v = G[v]
            seen.add(v)
            nodes.add(v)
            score += C[v]
            size += 1
        return score, size, nodes

    for i in range(N):
        if i in seen:
            continue
        score, size, nodes = calc_one_loop(i)
        if score == -1 and size == -1:
            continue
        loop_score.append(score)
        loop_size.append(size)
        loop_id2node[_id].extend(list(nodes))
        seen.add(i)
        _id += 1

    # print('loop_size: ', loop_size)
    # print('loop_score: ', loop_score)
    ans = -inf
    for i in range(_id):
        # i: id
        n_loop = K // loop_size[i]

        # score_afterを作る
        score_after = [[0] for _ in range(N)]
        for v in loop_id2node[i]:
            max_move_cnt = loop_size[i] + 1
            move_cnt = 0
            cum_score = 0
            cur_v = v
            while move_cnt < max_move_cnt:
                cur_v = G[cur_v]
                cum_score += C[cur_v]
                score_after[v].append(cum_score)
                move_cnt += 1
        # print('score_after: ', score_after)
        if loop_score[i] <= 0:
            max_step = min(K, loop_size[i])
            score = 0
        else:
            # 先に回る
            # ちょうど1周だったら、回らない
            score = 0
            max_step = loop_size[i]

            # if K == loop_size[i]:
            #     max_step = K
            #     score = 0
            # else:
            #     K -= n_loop * loop_size[i]
            #     max_step = K
            #     score = n_loop * loop_score[i]

        # loop_size[i]より小さい数で全探索
        for l in range(1, max_step + 1):
            for v in loop_id2node[i]:
                cp_score = score
                cnt = 0
                cp_score += score_after[v][l]
                # 実現不可能なら飛ばす
                if l > K:
                    continue
                # 回った時も試してみる
                if K - l >= loop_size[i]:
                    cp_score = max(cp_score, cp_score + loop_score[i] * ((K - l) // loop_size[i]))
                ans = max(ans, cp_score)
    print(ans)

main()

