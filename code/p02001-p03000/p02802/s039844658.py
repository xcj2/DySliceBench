#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def inputIntList():
  return [int(s) for s in input().split()]


def inputInt():
  return int(input())


def main():
  N, M = inputIntList()

  ac = 0
  wa = 0
  problem = [['', 0] for _ in range(N)]
  for _ in range(M):
    i, s = input().split()
    i = int(i)-1
    if problem[i][0] == 'AC':
      continue
    else:
      problem[i][0] = s

    if problem[i][0] == 'WA':
      problem[i][1] += 1
    else:
      ac += 1
  for result, wa_cnt in problem:
    if result == 'AC':
      wa += wa_cnt
  return '{} {}'.format(ac, wa)


if __name__ == "__main__":
  print(main())
