# coding: utf-8
import array, bisect, collections, copy, heapq, itertools, math, random, re, string, sys, time
sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7


def II(): return int(input())
def ILI(): return list(map(int, input().split()))
def IAI(LINE): return [ILI() for __ in range(LINE)]
def IDI(): return {key: value for key, value in ILI()}


def read():
    S = str(input())
    return (S,)


def solve(S):
    before_dict = collections.defaultdict(list)
    before_ind_dict = collections.defaultdict(int)
    for ind, char in enumerate(S):
        if char not in before_ind_dict:
            before_ind_dict[char] = ind
            before_dict[char].append(ind)
        else:
            before = before_ind_dict[char]
            before_dict[char].append(ind - before - 1)
            before_ind_dict[char] = ind

    len_s = len(S)
    for key, val in before_ind_dict.items():
        before_dict[key].append(len_s - val - 1)

    l_max = [max(v) for v in before_dict.values()]
    ans = min(l_max)
    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()
