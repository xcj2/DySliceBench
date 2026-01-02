n, a, b, c = map(int, input().split())
l = [int(input()) for i in range(n)]
goals = ['A', 'B', 'C', 'N']
from copy import copy
p = []

def search(i, goal, pre_abc):
  abc = copy(pre_abc)
  if goal == 'A':
    abc[0] += l[i]
  elif goal == 'B':
    abc[1] += l[i]
  elif goal == 'C':
    abc[2] += l[i]
  else:
    abc[3] += 1
  if i == len(l) - 1:
    if abc[0]!=0 and abc[1]!=0 and abc[2]!=0:
      p.append(abc)
  else:
    for goal in goals:
      search(i+1, goal, abc)
      
def mp(abc):
  return abs(abc[0]-a) + abs(abc[1]-b) + abs(abc[2]-c) + 10 * (n-3-abc[3])
      
def solve():
  for goal in goals:
    search(0, goal, [0,0,0,0])
  print(min(list(map(mp, p))))
  
solve()