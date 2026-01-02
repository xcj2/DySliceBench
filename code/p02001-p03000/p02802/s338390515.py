#!/usr/bin/env python3
import sys


def solve(N: int, M: int, p: "List[int]", S: "List[str]"):
    ok = 0
    penalty = 0

    problem_dict = {}
    for i in range(M):
        if problem_dict.get(p[i]) == None:
            problem_dict[p[i]] = [S[i]]
        else:
            problem_dict[p[i]].append(S[i])


    for key,value in problem_dict.items():
        if "AC" not in value:
            continue

        for result in value:
            if result == "WA":
                penalty += 1
            else:
                ok += 1
                break
    
    print(ok,penalty)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    p = [int()] * (M)  # type: "List[int]"
    S = [str()] * (M)  # type: "List[str]"
    for i in range(M):
        p[i] = int(next(tokens))
        S[i] = next(tokens)
    solve(N, M, p, S)

if __name__ == '__main__':
    main()
