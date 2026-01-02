#!/usr/bin/env python3
import sys

INF = 10**9

def solve(N: int, A: int, B: int, C: int, l: "List[int]"):
    def how_much_mp(cur, a, b, c):
        if cur == N: # 竹の材料が無でない
            return abs(A-a) + abs(B-b) + abs(C-c) -30 if min(a, b, c) > 0 else INF
        costs = []
        costs.append(how_much_mp(cur+1, a, b, c))
        costs.append(how_much_mp(cur+1, a+l[cur], b, c) + 10)
        costs.append(how_much_mp(cur+1, a, b+l[cur], c) + 10)
        costs.append(how_much_mp(cur+1, a, b, c+l[cur]) + 10)
        return min(costs)
    print(how_much_mp(0, 0, 0, 0))
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
    l = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A, B, C, l)

if __name__ == '__main__':
    main()
