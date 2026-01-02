# -*- coding: utf-8 -*-
# ALDS1_3_D_Areas on the Cross-Section Diagram

from collections import deque

def make_h_list(slope):
    """
    入力データから高さのリストを作る
    """
    h_list =deque([0])
    for s in slope:
        d = 0
        if s == "\\":
            d = -1
        elif s == "/":
            d = 1
        h_list.append(h_list[-1] + d)
    return h_list

def trim_edge(h_list, left=True):
    """
    水溜りの境界を探す
    """
    if left:
        while h_list:
            h = h_list.popleft()
            if h not in h_list:
                continue
            if h_list[0] - h < 0:
                h_list.appendleft(h)
                return h_list
    else:
        while h_list:
            h = h_list.pop()
            if h not in h_list:
                continue
            if h_list[-1] - h < 0:
                h_list.append(h)
                return h_list
            
def make_w_list(h_list):
    """
    水たまりのリストを作る
    """
    w_list = []
    water = []
    h_list = trim_edge(h_list)
    while h_list:
        h = h_list.popleft()
        if not water:
            water.append(h)
        elif water[0] == h:
            water.append(h)
            w_list.append(water)
            water = []
            h_list.appendleft(h)
            h_list = trim_edge(h_list)
        else:
            water.append(h)
            if water[0] < water[-1]:
                water.pop(0)
    return w_list
                
def calc_area(water):
    """
    面積計算
    """
    h = water[0]
    s = 0
    for i in range(len(water) - 1):
        s += (water[i+1] - h) + (water[i+1] - water[i]) / 2
    return abs(int(s))


in_data = str(input())

h_list = make_h_list(in_data)
h_list = trim_edge(h_list, left=False)

if type(h_list) != None:
    w_list = make_w_list(h_list)
    a_list = [calc_area(water) for water in w_list]
else:
    a_list = []

print(sum(a_list))
print(len(a_list), *a_list)
