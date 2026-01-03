#!/usr/bin/env python3
import sys
from collections import Counter

def solve(n: int, S: "List[str]"):
    counter_list = [Counter(S[i]) for i in range(n)]

    a = dict(counter_list[0].items())
    a_keys = list(counter_list[0].keys())
    for cl in counter_list[1:]:
        for key,value in list(cl.items()):
            if key in a_keys and a[key]>value:
                a[key] = value

    for cl in counter_list[1:]:
        for key in list(a.keys()):
            if key not in list(cl.keys()):
                a.pop(key)
    
    answer = ""
    for key,value in a.items():
        answer += key*value
    answer = list(answer)
    answer.sort()
    print("".join(answer))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(n)]  # type: "List[str]"
    solve(n, S)

if __name__ == '__main__':
    main()
