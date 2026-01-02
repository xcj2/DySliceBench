#!/usr/bin/env python3
import sys


def solve(N: int, M: int, V: int, P: int, A: "List[int]"):
    A.sort(reverse = True)

    used_vote = (P-1)*M
    res = M*V-used_vote

    # res を振り分けていく
    a = A[P-1:]
    r = a[0]+1
    l = -1
    while r - l > 1:
        mid = (r+l)//2
        goal = mid+M

        # 絶対入れない
        if a[0] > goal:
            l = mid
            continue

        need= 0 
        for aa in a:
            need+=min(M,goal-aa)
        
        if need >=res: ##成功
            r = mid
        else:
            l = mid
    
    # l が最小の値
    for i in range(N):
        if A[i] > l:
            continue
        else:
            print(i)
            return
    print(N)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    V = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, V, P, A)

if __name__ == '__main__':
    main()
