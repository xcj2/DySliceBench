import sys
import math
import numpy as np
sys.setrecursionlimit(10**7)

class Task:
    def __repr__(self):
        return str(self.__dict__)

    def time_toget_point(self, p):
        # p点とるのに必要な時間を返す
        if p >= self.max_minus:
            return math.ceil(self.b + (p - self.max_minus)/self.u)
        else:
            return math.ceil(p/self.l)

def solve():
    n, x = map(int, input().split())
    t_list = []
    total_behind = 0 # これだけ点を取らなければならない

    for i in range(n):
        t = Task()
        t.b, t.l, t.u = map(int, input().split())
        t.max_minus = t.b * t.l
        t.eff = ((x-t.b)*t.u) + (t.b*t.l) # 重み最高にした時の勉強効率
        t_list.append(t)
        total_behind += t.max_minus

    # 重み最高での勉強効率の降順に並び変え
    t_list = sorted(t_list, key=lambda t: t.eff, reverse=True)
    cumsum = list(np.cumsum([t.eff for t in t_list]))

    # 何要素目まで上から取ると必要点数を超えるか
    import bisect
    for max_i in range(len(t_list)):
        if cumsum[max_i] > total_behind:
            break

    # 部分点を取るtaskをi番目と決めたときの、必要勉強時間を求める。その最小値が答えになる
    min_time = -1
    for i, t in enumerate(t_list):
        if i <= max_i:
            # 上からとるものにiが含まれるケースでは、上から max_i 要素目までのうち i 以外を取り、iから最適な値をとる
            rest_p = total_behind - (cumsum[max_i] - t.eff)
        else:
            # 上からとるものにiが含まれないケースでは単に上から max_i-1 要素目までとり、iから最適な個数とる
            # rest_p が task i でとれる点数を超える場合があるが、解にはならないので気にしなくてよい
            if max_i == 0:
                rest_p = total_behind
            else:
                rest_p = total_behind - cumsum[max_i-1]

        # task i で rest_p とるのに必要な時間を求める
        time = x * (max_i) + t.time_toget_point(rest_p)

        if min_time == -1 or min_time > time:
            min_time = time
    print(min_time)

solve()