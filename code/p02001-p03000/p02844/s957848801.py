#!/usr/bin/env python3
import sys

def solve(N: int, S: str):
    answer = 0
    for i in range(1000):
        target = str(i).zfill(3)
        index = 0
        for i in range(N):
            if S[i] == target[index]:
                index += 1
            
            if index == 3:
                answer += 1
                break
    
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
