#!/usr/bin/env python3
import sys
import itertools

def solve(N: int, A: int, B: int, C: int, l: "List[int]"):
    # 0: 使わない 1:A 2:B 3:C
    all = list(itertools.product([0,1,2,3], repeat=N))
    answer = 10**9
    for a in all:
        a_sum = 0
        a_count = 0
        b_sum = 0
        b_count = 0
        c_sum = 0
        c_count = 0

        for i in range(len(a)):
            if a[i] == 0:
                continue
            elif a[i] == 1:
                a_sum += l[i]
                a_count +=1
            elif a[i] == 2:
                b_sum += l[i]
                b_count +=1
            elif a[i] == 3:
                c_sum += l[i]
                c_count +=1
        
        if a_count == 0 or b_count == 0 or c_count==0 :
            continue

        MP = (a_count-1)*10+(b_count-1)*10+(c_count-1)*10+abs(A-a_sum)+abs(B-b_sum)+abs(C-c_sum)

        answer = min(MP,answer)
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    l = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, C, l)

if __name__ == '__main__':
    main()
