#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, a: "List[int]", b: "List[int]"):
    A_sum = sum(a)
    B_sum = sum(b)
    if A_sum > B_sum:
        print(NO)
        return
    
    dif = [a[i]-b[i] for i in range(N)]
    one = 0
    two = 0
    for i in range(N):
        if dif[i] > 0:
            one += dif[i]
        if dif[i] < 0:
            two += -(dif[i]//2)
    
    if max(one,two) > B_sum-A_sum:
        print(NO)
    else:
        print(YES)
    # minimum_operations = []

    # for i in range(N):
    #     if dif[i] >= 0:
    #         minimum_operations.append(dif[i])
    #     else:
    #         minimum_operations.append(-(dif[i]//2))

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a, b)

if __name__ == '__main__':
    main()
