#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int, S: "List[str]"):
    """
    0は縦に入っている1は横に入っていることを表す
    """
    dominos = []
    i = 0
    while i < N:
        if S[0][i] == S[1][i]:
            dominos.append(0)
        else:
            dominos.append(1)
            i += 1
        i += 1

    answer = 3 if dominos[0] == 0 else 6
    for i in range(1,len(dominos)):
        if dominos[i] == 0 and dominos[i-1] == 0:
            answer *= 2
        elif dominos[i] == 1 and dominos[i-1] == 0:
            answer *= 2
        elif dominos[i] == 0 and dominos[i-1] == 1:
            answer *= 1
        elif dominos[i] == 1 and dominos[i-1] == 1:
            answer *= 3
        answer %= MOD
    print(answer%MOD)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(2)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()
