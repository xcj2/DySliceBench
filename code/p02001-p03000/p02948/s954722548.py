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
  L = []
  for i in range(N):
    a, b = map(int, input().split())
    L.append((a, b))
  L = sorted(L)

  H = []
  PQ = MaxHeap(H)
  max_ = 0

  start = 0
  for m in range(M-1, -1, -1):
    res = M - m
    while start < N and L[start][0] == res:
      PQ.heappush(L[start][1])
      start += 1

    if len(PQ):
      now = PQ.heappop()
      max_ += now

  print(max_)


if(__name__ == '__main__'):
  main()
