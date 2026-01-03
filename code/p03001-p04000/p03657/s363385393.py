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
 
# NO, PAY-PAY
#import numpy as np
#import statistics
#from statistics import mean, median,variance,stdev
 
def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))
 
def main():
    A,B = inputMap()
    
    if A % 3 == 0 or B % 3 == 0 or (A+B) % 3 == 0:
        print("Possible")
    else:
        print("Impossible")
        
if __name__ == "__main__":
	main()
