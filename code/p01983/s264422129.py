def parse_hash(s, pointer):
  head = s[pointer]
  if head == "[":
    pointer += 1
    op, pointer = parse_op(s, pointer)
    h1, pointer = parse_hash(s, pointer)
    h2, pointer = parse_hash(s, pointer)
    return calc(op, h1, h2), pointer + 1
  else:
    l, pointer = parse_letter(s, pointer)
    return l, pointer
 
def parse_op(s, pointer):
  return s[pointer], pointer + 1

def parse_letter(s, pointer):
  return int(s[pointer]), pointer + 1

def calc(op, h1, h2):
  if op == "+":
    return h1 | h2
  if op == "*":
    return h1 & h2
  if op == "^":
    return h1 ^ h2

from collections import defaultdict
from itertools import product
while True:
  s = input()
  if s == ".":break
  p = input()
  score = defaultdict(int)
  nums = [chr(i) for i in range(ord("0"), ord("9") + 1)]
  for a, b, c, d in product(nums, repeat=4):
    temp = s.replace("a", a)
    temp = temp.replace("b", b)
    temp = temp.replace("c", c)
    temp = temp.replace("d", d)
    score[parse_hash(temp, 0)[0]] += 1
  
  for i in range(4):
    s = s.replace(chr(ord("a") + i), p[i])
  hs = parse_hash(s, 0)
  print(hs[0], score[hs[0]])
