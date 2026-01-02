H, W, K = map(int, input().split())

S = [list(map(int, input())) for _ in range(H)]

C = [[0 for w in range(W)] for h in range(H)] #各行のw列目までに1が何個あるか

#print(S)
for h in range(H):
  for w in range(W):
    #print(h,w)
    C[h][w] = C[h][w-1] + S[h][w]

#print(C)
def settify(l):
  set_label = set()
  i = 0
  while l > 0:
    if l % 2 == 1:
      set_label.add(i)
    l //= 2
    i += 1
  return set_label
    
def set_label(s):
  tmp = 0
  for i in s:
    tmp += 2**i
  return tmp

def sum_set(s, w):
  s_list = list(s)
  s_list.sort()
  s_list.append(H-1)
  tmp = 0
  it = 0
  ans_list = []
  for h in range(H):
    tmp += C[h][w]
    #print(w, tmp)
    if h == s_list[it]:
      ans_list.append(tmp)
      tmp = 0
      it += 1
  return ans_list    
#print(sum_set(set(), 0), sum_set(set(), 1))
ans = 10**8
for l in range(2**(H-1)):
  s = settify(l)
  lt_prv = [0 for _ in range(len(s)+1)]
  lt_now = [0 for _ in range(len(s)+1)]
  lt_1minus = [0 for _ in range(len(s)+1)]
  tmp = len(s)
  w = 0
  w_prv = -1
  imp = False
  while w < W:
    lt_now = sum_set(s, w)
    flag = False
    for j in range(len(s)+1):
      if lt_now[j] - lt_prv[j] > K:
        flag = True
        break
    if flag:
      if w_prv == w-1:
        imp = True
      tmp += 1
      lt_prv = lt_1minus
      w_prv = w-1
    w += 1
    lt_1minus = lt_now
    if imp:
      break
    #print(s, w-1)
    #print(lt_prv, lt_1minus, lt_now)
  if not imp:
    ans = min(ans, tmp)
      
print(ans)
        
        
    
    
  
    
    



