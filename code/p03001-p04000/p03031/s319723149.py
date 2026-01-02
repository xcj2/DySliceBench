def count_one(num):
  ret = 0
  while num:
    if num & 1: ret+=1
    num = num >> 1

  return ret

def solve():
  N,M = map(int, input().split())
  switches = []
  for _ in range(M):
    switches_pattern = list(map(int, input().split()))[1:]
    pattern_int = sum(2**(i-1) for i in switches_pattern)
    switches.append(pattern_int)
  ps = list(map(int, input().split()))

  switch_pattern_upper = 2**N

  def check(pattern):
    ret = True
    for i in range(M):
      bit_count = count_one(switches[i] & pattern)
      # print(switches[i] & pattern, bit_count)
      if bit_count % 2 != ps[i]:
        ret = False
        break
      
    return ret
    
  ret = 0
  # print(switches)
  for pattern in range(switch_pattern_upper):
    # print(pattern)
    if check(pattern): ret += 1

  print(ret)
  
solve()