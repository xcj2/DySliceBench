import sys
import math
sys.setrecursionlimit(10**7)

debug = True
debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

class Task:
    def __repr__(self):
        return str(self.__dict__)
    def time_toget_point(self, p):
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

        t.max_minus = t.b * t.l # 重み最低で勉強しない場合のマイナス
        t.max_plus = (x-t.b) * t.u # 重み最高で満点まで勉強する時のプラス
        t.eff = t.max_plus + t.max_minus # 重み最高にした時の勉強効率
        t_list.append(t)

        total_behind += t.max_minus
    dprint(total_behind)

    # 重み最高での勉強効率の降順に並び変え
    import numpy as np
    t_list = sorted(t_list, key=lambda t: t.eff, reverse=True)
    cumsum = list(np.cumsum([t.eff for t in t_list]))
    dprint(t_list)
    dprint(cumsum)

    # 何要素目まで上から取ると必要点数を超えるか
    import bisect
    for max_i in range(len(t_list)):
        if cumsum[max_i] > total_behind:
            break
    dprint("max_i:", max_i)

    # 部分点を取るtaskをi番目と決めたときの、必要勉強時間を求める。その最小値が答えになる
    min_time = -1
    for i, t in enumerate(t_list):
        if i <= max_i:
            # このケースでは上から max_i 要素目までのうち i 以外を取り、iから最適な値をとる
            rest_p = total_behind - (cumsum[max_i] - t.eff)

        else:
            # このケースでは単に上から max_i-1 要素目までとり、iから最適な個数とる
            # 必要時間がXを超える場合は解にならないが、気にしなくていい
            if max_i == 0:
                rest_p = total_behind
            else:
                rest_p = total_behind - cumsum[max_i-1]

        time = x * (max_i) + t.time_toget_point(rest_p)
        dprint(i, rest_p, time, min_time, t)
        if min_time == -1 or min_time > time:
            min_time = time
    print(min_time)

solve()