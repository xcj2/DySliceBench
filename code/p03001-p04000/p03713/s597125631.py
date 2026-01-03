#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/24
Solved on 2019/3/
@author: shinjisu
"""


# ABC 062 C - Chocolate Bar
def getIntList(): return [int(x) for x in input().split()]
class Debug():
    def __init__(self):
        self.debug = True
 
    def off(self):
        self.debug = False
 
    def dmp(self, x, cmt=''):
        if self.debug:
            if cmt != '':
                print(cmt, ':  ', end='')
            print(x)
        return x

def prob():
    d = Debug()
    d.off()
    H, W = getIntList()
    d.dmp((H, W), 'H, W')

    # 縦か横の分割
    large1 = (H+2) // 3 * W
    small1 = H // 3 * W
    large2 = (W+2) // 3 * H
    small2 = W // 3 * H
    if large1-small1 < large2-small2:
        large, small = large1, small1
    else:
        large, small = large2, small2
    d.dmp((large, small), 'large, small')
    cand = large - small

    # 縦及び横の分割
    area = H*W
    d.dmp((area), 'area')
#    for i in range(area//large,  area//small+1):
    for i in range(max(1, min(H, W)//3),  (max(H, W)+1)//2+1):
        #d.dmp((i), 'i')
        div1 = i*W
        div2 = (H-i)*(W//2)
        div3 = (H-i)*((W+1)//2)
        #d.dmp((div1, div2, div3), 'div1, div2, div3')
        cand0 = max(div1, div2, div3) - min(div1, div2, div3)
        #d.dmp((cand0), 'cand0')
        cand = min(cand, cand0)
        div1 = i*H
        div2 = (W-i)*(H//2)
        div3 = (W-i)*((H+1)//2)
        #d.dmp((div1, div2, div3), 'div1, div2, div3')
        cand0 = max(div1, div2, div3) - min(div1, div2, div3)
        #d.dmp((cand0), 'cand0')
        cand = min(cand, cand0)
        #d.dmp((cand), 'cand')
    return cand


ans = prob()
if ans is None:
    pass
elif type(ans) == tuple and ans[0] == 1:  # 1,ans
    for elm in ans[1]:
        print(elm)
else:
    print(ans)
