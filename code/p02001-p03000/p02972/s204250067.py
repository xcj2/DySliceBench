#!/usr/bin/env python3
import sys

MOD = 2  # type: int


def solve(N: int, a: "List[int]"):
    answer = [0]*(N+1)
    for i in range(N,0,-1):
        for j in range(2*i,N+1,i):
            answer[i] += answer[j]
        if a[i-1]==1:
            answer[i]= 1 if answer[i]%2==0 else 0
        else:
            answer[i]= 0 if answer[i]%2==0 else 1
    print(sum(answer))

    answer2 = []
    for index,ans in enumerate(answer):
        if ans == 1:
            answer2.append(index)

    print(*answer2)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
