import math


swap_count = 0


def main():
  num = int(input())
  elements = []
  for i in range(0, num):
    elements.append(int(input()))

  # Get intervals
  interval = 1
  intervals = [interval]
  while True:
    interval = int_f(interval)
    if interval > num:
      break
    intervals.insert(0, math.ceil(interval))

  for interval in intervals:
    insertion_sort(elements, num, interval)

  print(len(intervals))
  print(' '.join([str(interval) for interval in intervals]))
  print(swap_count)
  for val in elements:
    print(val)


def int_f(x):
  return 2.25 * x + 1


def insertion_sort(elements, num, interval=1):
  global swap_count

  i = interval
  while i < num:
    j = i
    while interval <= j:
      if elements[j - interval] <= elements[j]:
        break

      elements[j - interval], elements[j] = elements[j], elements[j - interval]
      swap_count += 1
      j -= interval
    i += 1


if __name__ == '__main__':
  main()