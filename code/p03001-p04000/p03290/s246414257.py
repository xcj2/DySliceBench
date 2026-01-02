import sys
from collections import deque
import copy

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(D, G, inputs):
    problems = list(map(string_to_int, inputs))
    binary_max = 2 ** len(problems)

    min_num = -1
    for pattern in range(0, binary_max):
        binary_pattern = bin(pattern)[2:]
        while len(binary_pattern) != D:
            binary_pattern = '0' + binary_pattern

        incompleted_problem = -1
        count_num = 0
        count_score = 0

        for i in reversed(range(len(binary_pattern))):
            if binary_pattern[i] == '1':
                count_num += problems[i][0]
                count_score += (100 * (i+1)) * problems[i][0] + problems[i][1]
            elif incompleted_problem == -1 and binary_pattern[i] == '0':
                incompleted_problem = i

        if incompleted_problem != -1:
            for _ in range(problems[incompleted_problem][0]):
                if count_score >= G:
                    break
                count_num += 1
                count_score += 100 * (incompleted_problem+1)
        if count_score >= G and (min_num == -1 or count_num < min_num):
            min_num = count_num
    return min_num


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    [D, G] = string_to_int(input())
    ret = solve(D, G, inputs(D))
    print(ret)
