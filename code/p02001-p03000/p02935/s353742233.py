import sys, os
import collections
import heapq

MOD = 10 ** 9 + 7

def solve(input_stream):
  N = read_int(input_stream)
  values = read_ints(input_stream)
  heapq.heapify(values)
  while len(values) > 1:
    a,b = (heapq.heappop(values), heapq.heappop(values))
    heapq.heappush(values, (a+b)/2.0)
  return [str(heapq.heappop(values))]


def read_ints(input_stream):
  return [i for i in map(int, input_stream.readline().strip().split())]

def read_int(input_stream):
  return int(input_stream.readline().strip())


if __name__ == "__main__":
    outputs = solve(sys.stdin)
    for line in outputs:
      print(line)