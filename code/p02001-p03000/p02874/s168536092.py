#!/usr/bin/env python3
import sys

def solve(N: int, L: "List[int]", R: "List[int]"):
    LR= list(zip(L,R))
    LR.sort(key=lambda x:x[0])

    r_left_max = [] ##index 以下のrightのmin
    for lr in LR:
        if r_left_max:
            r_left_max.append(min(r_left_max[-1],lr[1]))
        else:
            r_left_max.append(lr[1])

    r_right_max = []
    for lr in LR[::-1]:
        if r_right_max:
            r_right_max.append(min(r_right_max[-1],lr[1]))
        else:
            r_right_max.append(lr[1])

    answer = 0
    for i in range(1,N):
        a = 0
        a += max(r_left_max[i-1]-LR[i-1][0]+1,0)
        a += max(r_right_max[N-i-1]-LR[-1][0]+1,0)
        answer = max(a,answer)

    ## 一つとその他の場合。indexがiのものを一つにする
    for i in range(N):
        a =0 
        a+= LR[i][1]-LR[i][0]+1
        if i == N-1:
            min_upper_limit = r_left_max[N-2]
            a+= max(min_upper_limit-LR[N-2][0]+1,0)
        elif i == 0:
            min_upper_limit = r_right_max[N-2]
            a+= max(min_upper_limit-LR[-1][0]+1,0)
        else:
            min_upper_limit = min(r_left_max[i-1],r_right_max[N-i-2])

            a+= max(min_upper_limit-LR[-1][0]+1,0)

        answer = max(a,answer)
    
    print(answer)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = [int()] * (N)  # type: "List[int]"
    R = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, L, R)

if __name__ == '__main__':
    main()
