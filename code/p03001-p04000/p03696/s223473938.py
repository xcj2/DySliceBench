#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    stack = []
    for i in range(N):
        if not stack:
            stack.append(S[i])
            continue

        if S[i] == "(":
            stack.append(S[i])
        else: ## )
            if stack[-1] == "(":
                stack.pop()
            else:
                stack.append(S[i])
    right_count = stack.count('(')
    left_count = stack.count(')')

    answer = '('*left_count+S+')'*right_count
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()
