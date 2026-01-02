#!/usr/bin/env python3

import sys


def main():
    # inf = float('inf')              # sys.float_info.max = 1.79e+308
    inf = 2 ** 63 - 1             # (for fast JIT compile in PyPy) 9.22e+18
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def input():  return sys.stdin.readline().rstrip()
    def ii():     return int(input())
    def isp():    return input().split()
    def mi():     return map(int, input().split())
    def mi_0():   return map(lambda x: int(x)-1, input().split())
    def lmi():    return list(map(int, input().split()))
    def lmi_0():  return list(map(lambda x: int(x)-1, input().split()))
    def li():     return list(input())
    def debug(x): print(x, file=sys.stderr)



    def calc_score(start):
        order = [None] * n
        accum = [None] * n
        order[start] = 0
        accum[start] = 0
        place = start
        cnt = 0
        current_score = 0
        M = -inf

        while cnt < k:
            place = P[place]    # 移動
            cnt += 1    # 移動回数
            current_score += C[place]    # 移動後の index でスコアに追加
            M = max(M, current_score)    # [スタートの次点, 現在地] まで任意の場所をゴールに選ぶときのスコア最大値
            if order[place] is None:
                # 未訪問
                order[place] = cnt
                accum[place] = current_score
            else:
                # 訪問ずみ (loop)
                head_len = order[place]
                loop_len = cnt - head_len
                head_score = accum[place]
                loop_gain = current_score - accum[place]
                if loop_gain <= 0:
                    # debug('encountered loop, but non-positive loop.')
                    return M
                else:
                    # debug('encountered positive loop.')
                    loop_times, res = divmod(k - head_len, loop_len)
                    # place からスタートして "0 以上" res 以下だけ進むときの
                    res_score = 0    # 稼ぐ最大スコア
                    tmp_score = 0    # 現在の累積スコア
                    tmp_place = place    # 現在地
                    for _ in range(res):
                        tmp_place = P[tmp_place]
                        tmp_score += C[tmp_place]    # 移動後の index でスコアに追加
                        res_score = max(res_score, tmp_score)
                    # 限界まで loop を回した上で 0 ~ res だけ貪欲に稼ぐ vs 限界 - 1 回 loop を回し確実にもう一回好きなところでとめられるようにして稼ぐ
                    loop_score = head_score + loop_times * loop_gain + res_score
                    stop_score = M + (loop_times - 1) * loop_gain
                    return max(loop_score, stop_score)

        # debug('never encountered loop.')
        return M
            

    n, k = mi()
    P = lmi_0()
    C = lmi()

    ans = -inf
    for i in range(n):
        score = calc_score(i)
        # debug(f'start: {i} ans: {score}')
        ans = max(ans, score)
    print(ans)


if __name__ == "__main__":
    main()
