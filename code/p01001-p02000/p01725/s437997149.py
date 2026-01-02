INF = 10 ** 20
ops = ["+", "-", "*"]
nums = [str(i) for i in range(0, 10)]
priorities = []
for op1 in ops:
  for op2 in ops:
    for op3 in ops:
      if op1 != op2 and op1 != op3 and op2 != op3:
        priorities.append([[op1], [op2], [op3]])
        priorities.append([[op1], [op2, op3]])
        priorities.append([[op1, op2], [op3]])
        priorities.append([[op1, op2, op3]])

def calc(num_lst, op_lst, priority):
  for x in range(len(priority)):
    while op_lst:
      for i, op in enumerate(op_lst):
        if op in priority[x]:
          if op == "+":
            num_lst = num_lst[:i] + [num_lst[i] + num_lst[i + 1]] + num_lst[i + 2:]
          elif op == "-":
            num_lst = num_lst[:i] + [num_lst[i] - num_lst[i + 1]] + num_lst[i + 2:]
          else:
            num_lst = num_lst[:i] + [num_lst[i] * num_lst[i + 1]] + num_lst[i + 2:]
          op_lst.pop(i)
          break
      else:
        break
  return num_lst[0]

def parse(s, priority):
  num_lst = []
  op_lst = []
  p = 0
  if s[p] == "(":
    p += 1
    num, addp = parse(s[p:], priority)
    num_lst.append(num)
    p += addp

  elif s[p] in nums:
    acc = ""
    while s[p] in nums:
      acc += s[p]
      p += 1
    num_lst.append(int(acc))
  
  while p < len(s) and s[p] != ")":
    op_lst.append(s[p])
    p += 1
    acc = ""
    if s[p] == "(":
      p += 1
      num, addp = parse(s[p:], priority)
      num_lst.append(num)
      p += addp
    else:
      #print(s[p])
      while s[p] in nums:
        acc += s[p]
        p += 1
      num_lst.append(int(acc))
  p += 1

  return (calc(num_lst, op_lst, priority), p)

def main():
  s = "(" + input() + ")"
  ans = -INF
  for priority in priorities:
    a, _ = parse(s, priority)
    ans = max(ans, a)
  print(ans)
main()
