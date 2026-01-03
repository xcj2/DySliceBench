#!/usr/bin/env python3
import sys
import itertools

def solve(n: int, a: "List[int]"):
    a_sum = list(itertools.accumulate(a))
    ## 一個目をマイナスにするバージョン
    dif1 = 0
    answer1 = 0
    for i in range(0,n):
        if i%2==0:
            if a_sum[i]+dif1>-1:
                answer1 += abs(-1-(a_sum[i]+dif1))
                dif1 += -1-(a_sum[i]+dif1)
        else:
            if a_sum[i]+dif1 <1:
                answer1 += abs(1-(a_sum[i]+dif1))
                dif1 += 1-(a_sum[i]+dif1)

    ## 一個目をプラスにするバージョン
    dif2 = 0
    answer2 = 0
    for i in range(0,n):
        if i%2==0:
            if a_sum[i]+dif2<1:
                answer2 += abs(1-(a_sum[i]+dif2))
                dif2 += 1-(a_sum[i]+dif2)
        else:
            if a_sum[i]+dif2>-1:
                answer2 += abs(-1-(a_sum[i]+dif2))
                dif2 += -1-(a_sum[i]+dif2)
        
    print(min(answer1,answer2))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    solve(n, a)

if __name__ == '__main__':
    main()
