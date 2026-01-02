"""
ALDS1_9_A
完全二分木を実装する
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
    

n = int(input())
heap_list = list(map(int, input().split()))+[None]*(n+1)


for i in range(n):
    k = heap_list[i]
    k_sentence = 'key = '+str(k)+', '
    if heap_list[get_parent(i)]:
        p = heap_list[get_parent(i)]
        p_sentence = 'parent key = '+str(p)+', '
    else:
        p_sentence = ''
    if heap_list[get_left(i)]:
        l = heap_list[get_left(i)]
        l_sentence = 'left key = '+str(l)+', '
    else:
        l_sentence = ''
    if heap_list[get_right(i)]:
        r = heap_list[get_right(i)]
        r_sentence = 'right key = '+str(r)+', '
    else:
        r_sentence = ''

    print('node '+str(i+1)+': '+k_sentence+p_sentence+l_sentence+r_sentence)






