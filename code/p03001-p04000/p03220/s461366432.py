#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Describe
"""
import numpy as np

def temp(height, t): 
    return t - 0.006 * height
   
def temp_to_height(a, t):
    return (t - a) / 0.006

def main():
    n = int(input())
    t, a = map(int, input().split())
    goal_height = temp_to_height(a, t)

    heights = list(map(int, input().split()))
    # print('heights: ', heights)
    # print('goal height: ', goal_height)


    best_index = -1
    best_diff = np.inf

    for i, h in enumerate(heights):
        diff = abs(h - goal_height)
        if diff < best_diff:
            best_diff = diff
            best_index = i
    best_number = best_index + 1

    print(best_number)
    
    

main()
