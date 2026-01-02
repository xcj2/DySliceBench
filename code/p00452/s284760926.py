from time import perf_counter
from itertools import combinations_with_replacement
from bisect import bisect_right
from functools import lru_cache


def solve1(darts, scores, point, target):
    if darts == 3 or point > target:
        if point > target:
            return 0
        else:
            pos = bisect_right(scores, target-point)
            return point + scores[pos-1]

    max_score = 0
    for s in scores:
        result1 = solve1(darts + 1, scores, point + s, target)  # ???????????´???
        # result2 = solve1(darts + 1, scores, point, target)      # ?????°????????£?????´???
        max_score = max(max_score, result1)
    return max_score


def solve2(darts, scores, point, target):
    """ ???????????? """
    combi = combinations_with_replacement(scores, 4)
    max_score = 0
    max_combi = []
    for s in combi:
        score = sum(s)
        if score <= target and score > max_score:
            max_score = score
            max_combi = s
    print('max_combi: {0}'.format(max_combi))
    return max_score


Target = 0
def solve3(darts, scores, point, target):
    """ ?????£???????????°??????????????¢??? """
    global Target
    Target = target
    return cache_solve3(darts, tuple(scores), point)


@lru_cache(maxsize=None)
def cache_solve3(darts, scores, point):
    if darts == 4 or point > Target:
        if point > Target:
            return 0
        else:
            pos = bisect_right(scores, Target-point)
            return point + scores[pos-1]

    max_score = 0
    for s in scores:
        result1 = cache_solve3(darts + 1, scores, point + s)
        max_score = max(max_score, result1)
    return max_score


def solve4(darts, scores, point, target):
    if darts == 3 or point > target:
        if point > target:
            return 0
        else:
            pos = bisect_right(scores, target-point)
            return point + scores[pos-1]

    max_score = 0
    t = (target - point) // (4 - darts)
    min_lim = bisect_right(scores, t)
    for s in range(min_lim-1, len(scores)):
        result1 = solve4(darts + 1, scores, point + scores[s], target)  # ???????????´???
        max_score = max(max_score, result1)
    return max_score


def solve5(darts, scores, point, target):
    combi = combinations_with_replacement(scores, 2)
    i_scores = [sum(x) for x in combi if sum(x) < target]
    i_scores.sort()

    results = [x + find_le(i_scores, target-x) for x in i_scores]
    return max(results)


def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError


if __name__ == '__main__':
    # ??????????????\???
    while True:
        N, M = [int(x) for x in input().split(' ')]
        scores = [int(input()) for _ in range(N)]

        if N == 0 and M == 0:
            break

        # ???????????????????????????????¨????
        scores.append(0)  # ??????????????????????????????????????¨??????????????¢???????????????????????????=0????????????
        scores.sort()  # ???????????°??????????????????????????????

        # start_time = perf_counter()
        # ans = solve1(0, scores, 0, M)
        # end_time = perf_counter()
        # print('solve1, elapsed: {0}'.format(end_time - start_time))
        # print(ans)

        # start_time = perf_counter()
        # ans = solve2(0, scores, 0, M)
        # end_time = perf_counter()
        # print('solve2, elapsed: {0}'.format(end_time - start_time))
        # print(ans)

        # start_time = perf_counter()
        # ans = solve4(0, scores, 0, M)
        # end_time = perf_counter()
        # print('solve4, elapsed: {0}'.format(end_time - start_time))
        # print(ans)

        #start_time = perf_counter()
        ans = solve5(0, scores, 0, M)
        #end_time = perf_counter()
        #print('solve5, elapsed: {0}'.format(end_time - start_time))
        print(ans)

        # ???????????¨???
        # print(ans)