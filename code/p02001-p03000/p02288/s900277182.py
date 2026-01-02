"""
ALDS1_9_B
最大ヒープを実装する
"""
import copy
import math

def get_parent(index):
    parent_index = math.floor((index-1)/2)
    return parent_index
    
def get_left(index):
    left_index = 2*index+1
    return left_index

def get_right(index):
    right_index = 2*index+2
    return right_index

def maxHeapify(A, i): #交換された時再帰関数で回す
    l = get_left(i)
    r = get_right(i)
    if A[l] and A[r]: #左も右も存在する時
        if l < n and A[l] > A[i]: #不等号は<（なぜなら，インデックスで与えてあるから
            largest = l
        else:
            largest = i
            
        if r < n and A[largest] < A[r]:
            largest = r
        
        if largest == i: #結局親が一番大きい時
            pass
        else:
            A[largest], A[i] = A[i], A[largest]
            maxHeapify(A, largest)
    
    elif not A[r]: #右の子がない時（左の子がない時は存在しない
        if l < n and A[l] > A[i]:
            A[l], A[i] = A[i], A[l]
            maxHeapify(A, l)
    
    else:
        pass



n = int(input())
heap_list = list(map(int, input().split()))+[None]*(n+1)

roop = math.floor(n/2)-1
for i in range(roop, -1, -1):
    maxHeapify(heap_list, i)


for i in range(n):
    k = heap_list[i]
    print(' '+str(k), end='')
print()

