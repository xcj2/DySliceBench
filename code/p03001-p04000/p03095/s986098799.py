from collections import defaultdict
import itertools
from functools import reduce


def analyze(string):
  s_count = defaultdict(int)
  for s in string:
    s_count[s] += 1
  counts = tuple(s_count.values())
  return counts

N = int(input())
string = input()

def search(N, string):
    memo = {}
    def count(counts, num_set):
        if (counts, num_set) in memo:
            return memo[(counts, num_set)]

        if num_set == 1:
            ans = sum(counts)
        elif num_set == 2:
            num_sum = sum(counts)
            ans = 0
            for i in range(len(counts)):
                num_sum -= counts[i]
                ans += counts[i] * num_sum
        else:
            ans = 0
            for i in range(len(counts) - 1):
                ans += counts[i] * count(counts[i + 1:], num_set - 1)

        memo[(counts, num_set)] = ans
        return ans

    counts = analyze(string)
    ans = 0
    for i in range(1, len(counts) + 1):
        ans += count(counts, i)
    print(ans % (10**9 + 7))

search(N, string)
