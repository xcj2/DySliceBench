N = int(input())
nums =list(map(int, input().split()))
a = {}
INF = 10**5
for num in nums:
  if not num in a:
    a[num] = 1
  else:
    a[num] += 1
  if len(a) > 3:
    print('No')
    exit()
def same_count(dic):
  v_max = 0
  v_min = INF
  for v in dic.values():
    v_max = max(v_max, v)
    v_min = min(v_min, v)
  return v_max == v_min
def xor_zero(dic):
  a = 0
  for k in dic.keys():
    a ^= k
  return True if a == 0 else False

def double_count(dic):
  v_max = 0
  v_min = INF
  for v in dic.values():
    v_max = max(v_max, v)
    v_min = min(v_min, v)
  return v_max == v_min*2 and dic[0] == v_min

answer = False
if len(a) == 3:
  answer = same_count(a) and xor_zero(a)
elif len(a) == 2:
  answer = 0 in a.keys() and double_count(a)
elif len(a) == 1:
  answer = 0 in a.keys()
if answer:
  print('Yes')
else:
  print('No')

  
    
