#総当たり
def calc(a, b, plus_minus):
  if plus_minus == 0:
    return a + b
  elif plus_minus == 1:
    return a - b

import itertools as it
list_prm = it.product([0, 1], repeat=3)
list_prm = list(list_prm)

list_abcd = [int(num) for num in input()]

def calc4(list_abcd, list_pm):
  ans = calc(list_abcd[0], list_abcd[1], list_pm[0])
  ans = calc(ans, list_abcd[2], list_pm[1])
  ans = calc(ans, list_abcd[3], list_pm[2])
  return ans

def serch_7(list_abcd, list_prm):
  for list_pm in list_prm:
    if calc4(list_abcd, list_pm) == 7:
      return list_pm

    
def convert(num):
  if num == 0:
    return "+"
  else:
    return "-"

sol = serch_7(list_abcd, list_prm)

s = str(list_abcd[0])
s += convert(sol[0])
s += str(list_abcd[1])
s += convert(sol[1])
s += str(list_abcd[2])
s += convert(sol[2])
s += str(list_abcd[3])
s += "=7"

print(s)   