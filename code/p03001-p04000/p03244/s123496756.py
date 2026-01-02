#!/usr/bin/env python3
import sys
from collections import Counter

def solve(n: int, v: "List[int]"):
    v1 = v[0::2]
    v2 = v[1::2]

    counter1 = Counter(v1).most_common(2)
    counter2 = Counter(v2).most_common(2)

    key1,value1 = counter1[0]
    key2,value2 = counter2[0]

    if key1 == key2:
        answer1 = 0
        ##1をかき変える
        if len(counter1)>=2:
            answer1 = len(v1)-counter1[1][1] +len(v2)-value2
        else:
            answer1 = len(v1) +len(v2)-value2

        answer2 = 0
        if len(counter1)>=2:
            answer2 = len(v1)-value1 +len(v2)-counter2[1][1]
        else:
            answer2 = len(v1)-value1 +len(v2)
        print(min(answer1,answer2))   
    else:
        print(len(v1)-value1+len(v2)-value2)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    v = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    solve(n, v)

if __name__ == '__main__':
    main()
