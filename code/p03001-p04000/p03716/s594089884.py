import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
import heapq

def make_score(l1, l2):
    h = []
    for num in l1:
        heapq.heappush(h, num)

    init_score = sum(h)

    v_temp = [0]
    v_max = [0]

    for num in l2:
        mini = heapq.heappop(h)
        score = num - mini
        heapq.heappush(h, num)
        v_temp.append(v_temp[-1] + score)
        if v_temp[-1] > v_max[-1]:
            v_max.append(v_temp[-1])
        else:
            v_max.append(v_max[-1])

    return init_score, v_max


def make_score_rev(l1, l2):
    h = []
    for num in l1:
        heapq.heappush(h, -num)

    init_score = -sum(h)

    v_temp = [0]
    v_max = [0]

    for num in l2:
        maxi = heapq.heappop(h) * -1
        score = maxi - num
        heapq.heappush(h, -num)
        v_temp.append(v_temp[-1] + score)
        if v_temp[-1] > v_max[-1]:
            v_max.append(v_temp[-1])
        else:
            v_max.append(v_max[-1])

    return init_score, v_max

n = getN()
nums = getList()


l1 = nums[:n]
l2 = nums[n:2*n]
l3 = nums[2*n:]

init_zen, v_max_zen = make_score(l1, l2)
init_kou, v_max_kou = make_score_rev(l3, l2[::-1])

# print(init_zen, init_kou)
# print(v_max_zen, v_max_kou)

t_score = 0
for i, j in zip(v_max_zen, v_max_kou[::-1]):
    if t_score < i + j:
        t_score = i + j

print(init_zen - init_kou + t_score)