N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]

def settify(j, n): #sが集合ラベル, nが多重度
  i = 0
  ans = [set() for _ in range(n)]
  while i < N:
    ans[j % n].add(i)
    i += 1
    j //= n
  return ans

def set_label(st): #setをlabel化する
  rtn = 0
  for j in st:
    rtn += 2**j 
  return rtn

def cost(s, L): #s:集合ラベル（使う竹）, L:目標長
  if s == 0:
    return 10**20
  st = settify(s, 2)[1]
  #print(st, s)
  l_first = 0
  for i in st:
    l_first += l[i] #とりあえず全部足す
  return 10*(len(st)-1) + abs(l_first - L) #最小コストを返す
  

#前準備
cost = [ 
  [cost(s2, A) for s2 in range(2**N)]
, [cost(s2, B) for s2 in range(2**N)]
, [cost(s2, C) for s2 in range(2**N)] ]

#print(cost)

mi = 10**20
for j in range(4**N):
  sets = settify(j, 4)
  q = [0, 0, 0]
  tmp = 0
  for p in range(3):
    tmp += cost[p][set_label(sets[p])]
  mi = min(mi, tmp)
  
print(mi)