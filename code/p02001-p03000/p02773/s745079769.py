#!/usr/bin/env python3
import sys
from collections import Counter

def solve(N: int, S: "List[str]"):
    counter = Counter(S).most_common()

    most_value = counter[0][1]
    answer_list = []

    for key,value in dict(counter).items():
        if value == most_value:
            answer_list.append(key)
    
    answer_list = list(set(answer_list))
    answer_list.sort()

    for i in range(len(answer_list)):
        print(answer_list[i])

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()
