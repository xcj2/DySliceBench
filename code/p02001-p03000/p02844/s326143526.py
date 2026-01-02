#!/usr/bin/env python3
import sys

def solve(N: int, S: str):
    answer = 0
    for i in range(0,1000):
        i = str(i).zfill(3)
        x = S.find(i[0])
        if x == -1:
            continue

        y = S.find(i[1],x+1)
        if y == -1:
            continue

        z = S.find(i[2],y+1)
        if z == -1:
            continue
        
        answer +=1
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
