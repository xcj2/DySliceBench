import sys
readline = sys.stdin.readline

# 0-indexでやる

D = int(readline())
C = list(map(int,readline().split())) # 満足度の下がりやすさ
S = [None] * D
sortS = [None] * D
for i in range(D):
  s = list(map(int,readline().split()))
  S[i] = s.copy()
  for j in range(len(s)):
    s[j] = (s[j],j)
  sortS[i] = sorted(s, key = lambda x:x[0], reverse = True)

def make_ans(D,C,limiter = 4, threshold = 2, balance = 0.5, check_limit = False):
  ans = []
  last_submit = [0] * 26
  for i in range(D):
    info = sortS[i]
    
    if check_limit:
    
      # limiter回以上提出がないものがあれば、threshold回を超えたもののうちCの値が高いものを提出
      if i - min(last_submit) >= limiter:
        ind = -1
        for j in range(len(last_submit)):
          if i - last_submit[j] >= threshold:
            if ind == -1:
              ind = j
            else:
              if C[ind] < C[j]:
                ind = j
        ans += [ind]
        last_submit[ind] = i
        continue
      
    topval = info[0][0]
    for j in range(len(info)):
      val = info[j][0]
      if check_limit:
        if val < topval * (balance):
          continue # 最高値の半分になるのであればやめよう
      index = info[j][1]
      if i - last_submit[index] < 26:
        continue
      ans += [index]
      last_submit[index] = i
      break
    else:
      ans += [info[0][1]]
  return ans

def calc_score(arr):
  point = 0
  last_submit = [0] * 26
  for i in range(len(arr)):
    # i日目
    point += S[i][arr[i]]
    for j in range(len(last_submit)):
      point -= (i - last_submit[j]) * C[j]
  return point
      
ans = make_ans(D,C)
#print(ans)
best = calc_score(ans)
for limiter in range(28,70):
  for threshold in range(26, limiter):
    for balance in (0.6,0.65,0.7,0.75,0.8,0.85,0.9):
      new_ans = make_ans(D,C,limiter,threshold,balance,True)
      new_score = calc_score(new_ans)
      if new_score > best:
        ans = new_ans
        best = new_score
  
def show(arr):
  for a in arr:
    print(a + 1)
    
show(ans)
