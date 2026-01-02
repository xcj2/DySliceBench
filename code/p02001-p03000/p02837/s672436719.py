import sys, os
import collections

class Dectation:
  def __init__(self, target, is_honest):
    super().__init__()
    self.target = target
    self.is_honest = is_honest

def solve(input_stream):
  number_of_people = read_int(input_stream)
  dectation_list = [[] for i in range(number_of_people)]

  for people_index in range(number_of_people):
    number_of_dectation = read_int(input_stream)
    for dectate_index in range(number_of_dectation):
      target_people, is_honest = read_ints(input_stream)
      dectation_list[people_index].append(Dectation(target_people, is_honest))
  ans = 0
  for bits in range(1, 1 << number_of_people):
    ok = True
    for index in range(number_of_people):
      if not ok:
        continue
      if ( ( (bits >> index) & 1 ) & 1) == 0:
        continue
      for dectation in dectation_list[index]:
        if (( bits >> (dectation.target - 1) ) & 1 ) ^ dectation.is_honest:
          ok = False
          break
    if ok:
      ans = max(ans, count(bits, 0))
  return [str(ans)]

def count(bits, ans):
  if bits == 0:
    return ans
  ans += bits & 1
  return count(bits >> 1, ans)

def read_ints(input_stream):
  return  map(int, input_stream.readline().strip().split())

def read_int(input_stream):
  return int(input_stream.readline().strip())

if __name__ == "__main__":
    outputs = solve(sys.stdin)
    for line in outputs:
      print(line)