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
    N = II()
    a = ILI()
    return (N, a)


def solve(N, a):
    a_lef = a[0: N]
    a_rig = [-i for i in a[2 * N: 3 * N]]
    heapq.heapify(a_lef)
    heapq.heapify(a_rig)
    sum_lef = sum(a_lef)
    sum_rig = sum(a_rig)
    l_sum_lef = [sum_lef]
    l_sum_rig = [sum_rig]
    
    for i in range(1, N + 1):
        heapq.heappush(a_lef, a[N - 1 + i])
        lef_pop = heapq.heappop(a_lef)
        sum_lef += a[N - 1 + i] - lef_pop
        l_sum_lef.append(sum_lef)
        
        heapq.heappush(a_rig, -a[2 * N - i])
        rig_pop = heapq.heappop(a_rig)
        sum_rig += -a[2 * N - i] - rig_pop
        l_sum_rig.append(sum_rig)

    ans = -INF

    for i in range(N + 1):
        num_dif = l_sum_lef[i] + l_sum_rig[N - i]
        ans = max(ans, num_dif)

    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()
