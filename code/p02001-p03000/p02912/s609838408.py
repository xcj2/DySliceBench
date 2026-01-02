from collections import defaultdict
from collections import deque
from collections import OrderedDict
import itertools
import heapq
from sys import stdin
input = stdin.readline


class MaxHeapObj(object):
  def __init__(self, val):
    self.val = val

  def __lt__(self, other):
    return self.val > other.val

  def __eq__(self, other):
    return self.val == other.val

  def __str__(self):
    return str(self.val)


class MinHeap(object):
  def __init__(self, L=None):
    if L is None:
      self.h = []
    else:
      heapq.heapify(L)
      self.h = L

  def heappush(self, x):
    heapq.heappush(self.h, x)

  def heappop(self):
    return heapq.heappop(self.h)

  def __getitem__(self, i):
    return self.h[i]

  def __len__(self):
    return len(self.h)


class MaxHeap(MinHeap):
  def __init__(self, L=None):
    super(MaxHeap, self).__init__(list(map(lambda x: MaxHeapObj(x), L)))

  def heappush(self, x):
    heapq.heappush(self.h, MaxHeapObj(x))

  def heappop(self):
    return heapq.heappop(self.h).val

  def __getitem__(self, i):
    return self.h[i].val


def main():
  N, M = list(map(int, input().split()))
  A = list(map(int, input().split()))

  PQ = MaxHeap(A)

  while M:
    now = PQ.heappop()
    PQ.heappush(int(now/2))
    M -= 1

  sum_ = 0
  for x in PQ.h:
    sum_ += x.val
  print(sum_)


if(__name__ == '__main__'):
  main()
