#!/usr/bin/env python3
import sys
def solve(N: int, D: "List[List[int]]"):
    count = 0
    flag = True
    for value in list(map(lambda k: k[0] == k[1], D)):
        if value:
            count += 1
        elif count < 3:
            count = 0
    ans = "Yes" if count >= 3 else "No"
    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = [[int(next(tokens)) for _ in range(2)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, D)

if __name__ == '__main__':
    main()
