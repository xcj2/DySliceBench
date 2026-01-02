# -*- coding: utf-8 -*-
import collections

def search_b(a_char, a_count, b_most_common, fixed_count):
  thres = fixed_count - a_count
  for (b_char, b_count) in [b for b in b_most_common if b[1] > thres]:
    if a_char != b_char:
      return a_count + b_count
  
  return fixed_count


def search(a_most_common, b_most_common):
  fixed_count = -1
  b_max = b_most_common[0][1]

  for (a_char, a_count) in a_most_common:
    if a_count <= fixed_count - b_max:
      break

    fixed_count = search_b(a_char, a_count, b_most_common, fixed_count)
  
  return fixed_count


def main():
  n = int(input())
  V = list(map(int, input().split()))

  a = V[::2]
  b = V[1::2]
  
  a_counter = collections.Counter(a)
  b_counter = collections.Counter(b)

  a_most_common = a_counter.most_common()
  b_most_common = b_counter.most_common()

  if len(a_most_common) == 1 and len(b_most_common) == 1 and a_most_common[0][0] == b_most_common[0][0]:
    print(n // 2)
    return

  print(n - search(a_most_common, b_most_common))


if __name__ == '__main__':
  main()
