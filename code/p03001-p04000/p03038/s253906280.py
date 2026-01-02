from __future__ import print_function
import sys
input = sys.stdin.readline

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# import numpy as np
# import numpypy as np

# import math
# import string
# import fractions
# import re
# import array
# import copy
# import functools
# import operator
# import queue
from queue import Queue
# from queue import PriorityQueue as PQueue

# import collections
# import itertools
# import bisect
# import heapq

from heapq import heappush
from heapq import heappop
from heapq import heapify
# from itertools import accumulate
# from collections import deque
# import random


class PQueue (Queue):
    '''Variant of Queue that retrieves open entries in priority order (lowest first).
    Entries are typically tuples of the form:  (priority number, data).
    '''
    def _init(self,maxsize=0):
        self.queue = []

    def set(self,x_queue):
        self.queue=x_queue
    def _qsize(self):
        return len(self.queue)

    def _put(self, item):
        heappush(self.queue, item)

    def _get(self):
        return heappop(self.queue)


def main():
    # 
    n,m = map(int, input().split())
    cards = list(map(lambda x:x,(map(int, input().split()))))
    # eprint(cards)
    heapify(cards)
    # eprint(sum(cards))
    # eprint("cards",cards)
    
    pq = PQueue()
    pq.set(cards)
    # print(pq)
    # eprint(pq.qsize())
    # while pq.qsize():
        # eprint(pq.get())


    # 
    tuple_list = []
    for i in range(m):
        b,c = map(int, input().split())
        tuple_list.append([c,b])
    tuple_list.sort()
    # eprint(tuple_list)



    cnt=0
    while cnt<n and len(tuple_list):
        temp=tuple_list.pop()
        # eprint(temp[1])
        while temp[1]>0:
            # eprint("WTF")
            pq.put(temp[0])
            if pq.qsize()>n:
                pq.get()
            cnt+=1
            temp[1]-=1

    print(sum(pq.queue))
if __name__ == '__main__':
    main()

###
# n==10^5枚のカードを，m==10^5回の操作で置き換えていく
# 
# 
# 
