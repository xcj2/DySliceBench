#!/usr/bin/env python3
import sys
import itertools

def solve(N: int):
    LEN = len(str(N))
    if LEN <= 2:
        print(0)
        return

    answer = 0
    for i in range(3,LEN+1):
        for num in list(itertools.product(['3','5','7'], repeat=i)):

            if num.count('3') >= 1 and num.count('5')>=1 and num.count('7') >=1 and int(''.join(num))<=N:
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
    solve(N)

if __name__ == '__main__':
    main()
