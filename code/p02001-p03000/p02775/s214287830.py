#!/usr/bin/env python3
import sys

def solve(N: str):
    n = list(map(int,list(N)))
    kuriage = 0
    LEN = len(n)
    pay_count = 0

    for i in range(LEN-1,-1,-1):
        if i != 0:
            if n[i-1] >= 5:
                if n[i]+kuriage <= 4:
                    pay_count += n[i]+kuriage
                    kuriage = 0
                else:
                    pay_count += 10-(n[i]+kuriage)
                    kuriage = 1
            else:
                if n[i]+kuriage <= 5:
                    pay_count += n[i]+kuriage
                    kuriage = 0
                else:
                    pay_count += 10-(n[i]+kuriage)
                    kuriage = 1
        else:
            if n[i]+kuriage <= 5:
                pay_count += n[i]+kuriage
                kuriage = 0
            else:
                pay_count += 10-(n[i]+kuriage)
                kuriage = 1

    if kuriage == 1:
        pay_count += 1
    print(pay_count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = next(tokens)
    solve(N)

if __name__ == '__main__':
    main()
