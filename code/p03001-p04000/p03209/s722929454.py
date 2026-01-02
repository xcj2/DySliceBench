import sys

sys.setrecursionlimit(50000)


n, x = map(int, input().split())

sum_berger = {0: 1}


# 考え方 xがレベルいくつのバーガーのどの位置かを考える
# レベルnのバーガー = "B" + レベルn-1のバーガー + "P" + レベルn-1のバーガー + "B"
# という式から再帰的にどのバーガーにいるかを考える。
def recursive(n):
    if n in sum_berger.keys():
        return sum_berger[n]
    else:
        sum_berger[n] = 1 + recursive(n - 1) + 1 + recursive(n - 1) + 1
        return sum_berger[n]


patties = {0: 1}


def patti(n):
    if n in patties.keys():
        return patties[n]
    else:
        patties[n] = patti(n - 1) * 2 + 1
        return patties[n]


def answer(n, x):
    if x == 1:
        if n == 0:
            return 1
        else:
            return 0
    elif x == sum_berger[n]:
        return patties[n]
    elif x < sum_berger[n] // 2+1:
        return answer(n-1, x-1)
    elif x == sum_berger[n] // 2 + 1:
        return patties[n] // 2 + 1
    elif x > sum_berger[n] // 2 + 1:
        return answer(n-1, x-(sum_berger[n] // 2 + 1)) + patties[n] // 2 + 1


patti(50)
recursive(50)

print(answer(n, x))
# BBBBPPPBPBPPPBBPBBPPPBPBPPPBBBPBBBPPPBPBPPPBBPBBPPPBPBPPPBBBB
# BBBPPPBPBPPPBBPBBPPPBPBPPPBBB
# BBPPPBPBPPPBB
# BPPPB
# P