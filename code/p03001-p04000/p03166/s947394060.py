#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	G
# CreatedDate:  2020-05-18 17:21:29 +0900
# LastModified: 2020-05-19 01:07:59 +0900
#


import os
import sys
from collections import deque
#import numpy as np
#import pandas as pd
def chmax(s,t):
    if s<t:
        return t
    else:
        return s


def longest_path(ans_list,node_list,lon_path):
    while ans_list:
        u = ans_list.pop()
        for v,_from in enumerate(node_list):
            if u in _from and lon_path[v]<lon_path[u]+1:
                lon_path[v]=lon_path[u]+1
    print(max(lon_path))

def main():
    n,m = map(int,input().split())
    node_list = [[] for _ in range(n+1)]
    to_count = [0]*(n+1)
    for _ in range(m):
        s,t = map(int,input().split())
        node_list[s].append(t)
        to_count[t]+=1
    q = deque()
    for i,x in enumerate(to_count):
        if x==0:
            q.append(i)
    q.popleft()
    distance = [0]*(n+1)
    ans_list = []
    while q:
        u = q.popleft()
        for v in node_list[u]:
            to_count[v]-=1
            if to_count[v]==0:
                q.append(v)
                distance[v]=chmax(distance[v],distance[u]+1)
        ans_list.append(u)
    print(max(distance))
#    longest_path(ans_list,node_list,lon_path)

if __name__ == "__main__":
    main()
