import sys
from pprint import pprint
import heapq

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(N, M, inputs):
    jobs = list(map(string_to_int, inputs))
    jobs.sort(key=lambda x: x[0], reverse=True)
    selectable = []
    money = 0
    for day in range(1, M + 1):
        while len(jobs) != 0 and jobs[-1][0] <= day:
            heapq.heappush(selectable, jobs.pop()[1] * -1)
        if len(selectable) != 0:
            money += heapq.heappop(selectable) * -1
    return money


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [N, M] = string_to_int(input())
    ret = solve(N, M, inputs(N))
    print(ret)
