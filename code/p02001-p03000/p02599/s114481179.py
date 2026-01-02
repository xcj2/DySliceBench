
import sys
input = sys.stdin.readline

def update(index, value, bit):
  #print('update', index, value)
  while index < len(bit):
    #print('update', index)
    bit[index] += value
    index += index & -index
  #print('done')
    
    
def cumsum(index, bit):
  ans = 0
  while index > 0:
    #print('cumsum', index)
    ans += bit[index]
    index -= index & -index
  #print('done', ans)
  return ans
  

def main():
  N, q = [int(x) for x in input().split()]
  C = [int(x)-1 for x in input().split()]
  Q = []
  for i in range(q):
    l, r =  [int(x)-1 for x in input().split()]
    Q.append((i, l, r))
  Q.sort(key=lambda x: x[2])
  leftmost = [-1] * N
  bit = [0] * (N+1)
  prev = -1
  ans = [0] * q
  for i, l, r in Q:
    #print(i, r, l)
    to_update = {}
    for x in range(prev+1, r+1):
      to_update[C[x]] = x
    for c, x in to_update.items():
      if leftmost[c] >= 0:
        update(leftmost[c] + 1, -1, bit)
      leftmost[c] = x
      update(x + 1, 1, bit)
    prev = r
    #print(i, r, l)
    #print(C)
    #print([cumsum(i, bit) for i in range(1, N+1)])
    ans[i] = cumsum(r + 1, bit) - cumsum(l, bit)
    
  for a in ans:
    print(a)
  

main()