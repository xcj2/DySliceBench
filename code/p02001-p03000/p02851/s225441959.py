import sys, os
import collections

MOD = 10 ** 9 + 7

def solve(input_stream):
  N, K  = read_ints(input_stream)
  numbers = [int(i) - 1 for i in input_stream.readline().strip().split()]
  cumulative_sum = [0 for i in range(N + 1)]
  mods = {}
  ans = 0
  for index, number in enumerate(numbers):
    cumulative_sum[index + 1] = (cumulative_sum[index] + number) % K
  queue = []
  
  for index in range(N+1):
    if cumulative_sum[index] not in mods:
      mods[cumulative_sum[index]] = 0
    ans += mods[cumulative_sum[index]]
    mods[cumulative_sum[index]] += 1
    queue.append(cumulative_sum[index])
    if len(queue) == K:
      target = queue.pop(0)
      mods[target] -= 1
  return [str(ans)]

  


def read_ints(input_stream):
  return [i for i in map(int, input_stream.readline().strip().split())]

def read_int(input_stream):
  return int(input_stream.readline().strip())


if __name__ == "__main__":
    outputs = solve(sys.stdin)
    for line in outputs:
      print(line)