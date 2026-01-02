import numpy as np
n = int(input())

def plus_idx(num):
  return 2 * int(np.ceil(np.log2(1 + 3*num)/2)) - 2

def minus_idx(num):
  return 2 * int(np.ceil(np.log2(1 + 3 * abs(num) / 2)/2)) - 1

def return_idx(num):
  if num == 0:
    return 0
  elif num > 0:
    return plus_idx(num)
  else:
    return minus_idx(num)
    
def minus_two_recur(num, l):
  if num == 0:
    return 0, l
  elif num > 0:
    idx = plus_idx(num)
    l[-(idx+1)] = 1
    new_num = num - (-2)**idx
    return new_num, l
  elif num < 0:
    idx = minus_idx(num)
    l[-(idx+1)] = 1
    new_num = num - (-2)**idx
    return new_num, l

num = n
max_length = return_idx(num)
result = [0] * (max_length+1)
while num != 0:
  num, result = minus_two_recur(num, result)

print("".join(map(str,result)))