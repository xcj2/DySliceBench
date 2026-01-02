#!/usr/bin/env python3
import sys
import bisect

def solve(N: int, K: int, V: "List[int]"):
    a = 0
    answer = []
    reverse_V = V[::-1]
    for i in range(1,min(N,K)+1): ##iコまで宝石をとる
        for left in range(i+1): ##左からleftこ
            right = i-left
            if left>0 and right>0:
                answer =  V[:left]+reverse_V[:right]
            elif left>0:
                answer = V[:left]
            elif right>0:
                answer = V[:right]
            else:
                answer = []
            answer.sort()
            zero_index = bisect.bisect_left(answer,0)
            # 小さいものからK-iこすてる
            answer = answer[min(zero_index,K-i):]
            a = max(a,sum(answer))
    
    print(a)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    V = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, V)

if __name__ == '__main__':
    main()
