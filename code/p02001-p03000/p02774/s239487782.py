import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def nC2(n):
    return n * (n-1) // 2

n,k = get_nums_l()
aaa = get_nums_l()

negatives = []
zeros = 0
positives = []

for a in aaa:
    if a == 0:
        zeros += 1
    elif a > 0:
        positives.append(a)
    else:
        negatives.append(a)

# 絶対値小さい順
positives.sort()
negatives.sort(reverse=True)

len_positives = len(positives)
len_negatives = len(negatives)

p_zeros = zeros*(len_negatives+len_positives) + nC2(zeros)
p_positives = nC2(len_positives) + nC2(len_negatives)
p_negatives = len_positives * len_negatives

log(len_negatives, zeros, len_positives)
log(p_negatives, p_zeros, p_positives)

if p_negatives < k <= (p_negatives+p_zeros):
    print(0)
    exit()

if k <= p_negatives:
    # 負の場合
    nokori = k
    log("nokori", nokori)

    left = -1 * ((10**9)**2 + 1)
    right = -1

    # 積がcenter未満になるペアがnokori個未満になる最大のcenterを探す
    while left < right:
        center = (left+right+1) // 2
        # log("center", center)

        left2 = len_positives-1
        right2 = len_negatives-1

        count = 0

        while right2 > 0 and positives[left2] * negatives[right2] < center:
            right2 -= 1
        
        # log("right2", right2)

        while 0<=left2<len_positives and 0<=right2<len_negatives:
            # log(positives[left2] * negatives[right2])
            if positives[left2] * negatives[right2] < center:
                count += len_negatives - right2
                left2 -= 1
            else:
                right2 += 1

        # left2 = len_positives-1
        # right2 = len_negatives-1

        # while left2 > 0 and positives[left2] * negatives[right2] < center:
        #     left2 -= 1
        # while right2 >= 0 and left2 < len_positives and (len_positives-left2 < len_negatives-right2):
        #     log(positives[left2] * negatives[right2])
        #     if positives[left2] * negatives[right2] < center:
        #         count += len_positives - left2
        #         right2 -= 1
        #     else:
        #         left2 += 1
        
        # log("count", count)
        if count < nokori:
            left = center
        else:
            right = center - 1
    print(left)
    exit()

# 正の場合
nokori = k - p_negatives - p_zeros
# log("nokori", nokori)

left = 1
right = (10**9)**2 + 1

# 積がcenter未満になるペアがnokori個未満になる最大のcenterを探す
while left < right:
    center = (left+right+1) // 2
    # log("center", center)

    left2 = 0
    right2 = len_positives-1

    count = 0

    while left2 < right2:
        if positives[left2] * positives[right2] < center:
            count += right2 - left2
            left2 += 1
        else:
            right2 -= 1

    left2 = 0
    right2 = len_negatives-1

    while left2 < right2:
        if negatives[left2] * negatives[right2] < center:
            count += right2 - left2
            left2 += 1
        else:
            right2 -= 1
    
    # log("center", center, "count", count)

    if count < nokori:
        left = center
    else:
        right = center-1
print(left)