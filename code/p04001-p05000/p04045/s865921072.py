def equal(n, available):
  return n in available 

def less(n, available):
  return n < sorted(available, reverse=True)[0]

def greater(n, available):
  return n > sorted(available, reverse=True)[0]
  

#less(n, available) == True であること
def upper_next(n, available):  
  for v in sorted(available):
    if n < v:
      return v
  return 1/0

  
n_str, _ = [v for v in input().split()]
n_s = [0]
n_s.extend([int(n_str[i:i+1]) for i in range(len(n_str))])
#print(n_s)
d_s = [int(v) for v in input().split()]

available = set(list(range(10))) - set(d_s)

#print("n", n_s, "d", d_s, "u", available)

min_available = sorted(available)[0]
max_available = sorted(available, reverse=True)[0]
#print(min_available, max_available)
ans = [0]
ans.extend([min_available] * (len(n_s) - 1))

eq = True
for i in range(1, len(n_s)):
  #print(ans)
  if eq:
    if equal(n_s[i], available):
      ans[i] = n_s[i]
      continue
    else:
      eq = False
      #print(n_s[i], available)
      if less(n_s[i], available):
        ans[i] = upper_next(n_s[i], available)
        #残りは最小値詰め
        break
      else:
        for j in range(i - 1, -1, -1):
          #print(ans)
          if ans[j] == max_available:
            ans[j] = min_available
          else:
            #print(ans)
            ans[j] = upper_next(ans[j], available)
            #print(ans)
            break
        break

#print(ans)
begin = 0
if ans[0] == 0:
  begin = 1
ans_val = "".join(map(lambda x:str(x), ans[begin:]))

print(ans_val)