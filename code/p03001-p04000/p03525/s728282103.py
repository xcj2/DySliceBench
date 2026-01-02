#!/usr/bin/env python3
import sys
from collections import Counter
import itertools
import copy

def solve(N: int, D: "List[int]"):
    counter = dict(Counter(D+[0]))
    time = [False]*25
    once = []
    # 枝狩り処理
    for i in range(13): 
        if counter.get(i) == None:
            continue
        if counter[i] == 2:
            if i == 0:
                print(0)
                return
            time[12+i] = True
            time[12-i] = True
        elif counter[i] >= 3: #どう頑張っても時刻のさの最大値は0
            print(0)
            return
        else:
            # if i != 0:
            once.append(i)

    LEN = len(once)
    bit_list = list(itertools.product([0, 1], repeat=LEN))

    if LEN == 0:
        min_dif = 12        
        time = [i for i,t in enumerate(time) if t]
        for first,second in list(itertools.combinations(time,2)):
            min_dif = min(min_dif,min(abs(first-second),24-abs(first-second)))
        print(min_dif)
        return

    answer = 0

    # onceを進んでるか戻ってるかのどちらかに振り分けていく
    for bit in bit_list:
        tmp = copy.deepcopy(time)
        
        for i in range(LEN): # 1なら進んでる0なら戻ってる
            if bit[i] == 1:
                tmp[12+once[i]] = True
            else:
                tmp[12-once[i]] = True

        # Trueのものだけ抜き出す
        tmp = [i for i,t in enumerate(tmp) if t]
        min_dif = 12
        for first,second in list(itertools.combinations(tmp,2)):
            min_dif = min(min_dif,min(abs(first-second),24-abs(first-second)))
        answer = max(min_dif,answer)

    print(answer)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, D)

if __name__ == '__main__':
    main()
