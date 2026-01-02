#!/usr/bin/env python3
import sys


def solve(s: str, K: int):

    index_dict = {}
    for i in range(len(s)):
        if index_dict.get(s[i]) == None:
            index_dict[s[i]] = [i]
        else:
            index_dict[s[i]].append(i)

    value_list = sorted(set(list(s)))
    candidate = set()

    for string in value_list:
        index = index_dict[string]
        for i in index:
            tmp_s = ""
            for j in range(i,len(s)):
                if len(tmp_s) > K:
                    break
                tmp_s += s[j]
                candidate.add(tmp_s)
        if len(candidate) >= K:
            break
    candidate = list(candidate)
    candidate.sort()
    print(candidate[K-1])

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    solve(s, K)

if __name__ == '__main__':
    main()
