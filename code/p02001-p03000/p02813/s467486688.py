# -*- coding: utf-8 -*-
import sys

def sort(P, Q):
    N = len(P)
    for i in range(N):
        if P[i] < Q[i]:
            return (P, Q)
        elif P[i] > Q[i]:
            return (Q, P)
    else:
        return (-1, -1)

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

    return array

def get_next_bigger(array):
    N = len(array)
    # 最後尾から要素iと要素i-1を比較して「要素i-1 < 要素i」のiを探す
    for i in reversed(range(N)):
        if array[i-1] < array[i]:
            # array[i:N]の中で、array[i-1]より大きい要素でかつ最小の要素をarray[i-1]と入れ替える
            minimum_number = N + 1
            minimum_element = i-1
            for j in range(i, N):
                if array[i-1] < array[j] and minimum_number > array[j]:
                    minimum_number = array[j]
                    minimum_element = j
            temp_array = swap(array, i-1, minimum_element)
            new_array = temp_array[:i]
            temp_array2 = temp_array[i:]
            temp_array2.sort()
            new_array.extend(temp_array2)
            return new_array

N = int(input())
P = [int(i) for i in input().split()]
Q = [int(i) for i in input().split()]

# 辞書順で小さいほうを選択
(minimum, maximum) = sort(P, Q)

if minimum == -1:
    print(0)
    sys.exit()

# 小さいほうを一つずつ大きくしてもう一方と同じになるまでの手数が答え
distance = 0
while True:
    if minimum == maximum:
        break
    else:
        distance += 1
    
    # minimumを一つ大きくする
    new_minimum = get_next_bigger(minimum)
    minimum = new_minimum

print(distance)