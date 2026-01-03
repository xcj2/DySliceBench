# -*- coding: utf-8 -*-
import sys
import copy
import collections
from bisect import bisect_left
from bisect import bisect_right
from collections import defaultdict
from heapq import heappop, heappush
import math
import itertools
import random
 
# NO, PAY-PAY
#import numpy as np
#import statistics
#from statistics import mean, median,variance,stdev
 
def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))
 
def main():
    H,W = inputMap()
    
    if H % 3 == 0 or W % 3 == 0:
        print(0)
        sys.exit()
        
    if H <= 2 and W <= 2:
        print(1)
        sys.exit()
        
    a = -(-W // 3)
    b = -(-H // 2)
    s1 = a * H
    s2 = (W-a) * b
    s3 = (W-a) * (H-b)
    ans1 = max(s1,s2,s3)-min(s1,s2,s3)
    
    a -= 1
    s1 = a * H
    s2 = (W-a) * b
    s3 = (W-a) * (H-b)
    ans2 = max(s1,s2,s3)-min(s1,s2,s3)
    
    a += 2
    s1 = a * H
    s2 = (W-a) * b
    s3 = (W-a) * (H-b)
    ans3 = max(s1,s2,s3)-min(s1,s2,s3)
    
    ans = min(ans1,ans2,ans3)
    
    tmp = W // 3
    tmp2 = (W - tmp) // 2
    s1 = tmp * H
    s2 = tmp2 * H
    s3 = (W - tmp- tmp2) * H
    ans1 = max(s1,s2,s3)-min(s1,s2,s3)
    
    tmp += 1
    s1 = tmp * H
    s2 = tmp2 * H
    s3 = (W - tmp- tmp2) * H
    ans2 = max(s1,s2,s3)-min(s1,s2,s3)
    
    tmp -= 2
    s1 = tmp * H
    s2 = tmp2 * H
    s3 = (W - tmp- tmp2) * H
    ans3 = max(s1,s2,s3)-min(s1,s2,s3)
    
    ansans = min(ans,ans1,ans2,ans3)
    
    a = -(-H // 3)
    b = -(-W // 2)
    s1 = a * W
    s2 = (H-a) * b
    s3 = (H-a) * (W-b)
    ans1 = max(s1,s2,s3)-min(s1,s2,s3)
    
    a -= 1
    s1 = a * W
    s2 = (H-a) * b
    s3 = (H-a) * (W-b)
    ans2 = max(s1,s2,s3)-min(s1,s2,s3)
    
    a += 2
    s1 = a * W
    s2 = (H-a) * b
    s3 = (H-a) * (W-b)
    ans3 = max(s1,s2,s3)-min(s1,s2,s3)
    
    ans = min(ans1,ans2,ans3)
    
    tmp = H // 3
    tmp2 = (H - tmp) // 2
    s1 = tmp * W
    s2 = tmp2 * W
    s3 = (H - tmp- tmp2) * W
    ans1 = max(s1,s2,s3)-min(s1,s2,s3)
    
    tmp += 1
    s1 = tmp * W
    s2 = tmp2 * W
    s3 = (H - tmp- tmp2) * W
    ans2 = max(s1,s2,s3)-min(s1,s2,s3)
    
    tmp -= 2
    s1 = tmp * W
    s2 = tmp2 * W
    s3 = (H - tmp- tmp2) * W
    ans3 = max(s1,s2,s3)-min(s1,s2,s3)
    
    print(min(ans,ans1,ans2,ans3,ansans))
	
if __name__ == "__main__":
	main()
