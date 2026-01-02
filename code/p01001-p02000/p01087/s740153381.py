import re
def dotexit(s):
  return re.sub("^\.","",s)

def prod(l):
  x=1
  for i in l:
    x *= i
  return x

def rec(s):
  nums=[dotexit(x) for x in s[1:]]
  ad = []
  for i in range(len(nums)):
    if nums[i]=='+' or nums[i]=='*':
      rl=[nums[i]]
      for j in range(i+1,len(nums)):
        if nums[j][0] == '.':
          rl.append(nums[j])
        else:
          break
      ad.extend(rec(rl))
  nums.extend(ad)
  nums = [x for x in nums if x !='+' and x != '*' and x[0]!='.']
  if s[0]=='+':
    return [str(sum([int(x) for x in nums]))]
  elif s[0]=='*':
    return [str(prod([int(x) for x in nums]))]
  else:
    return s

while True:
  n=int(input())
  if n==0:
    break
  s=[]
  for i in range(n):
    s.append(input())
  print(rec(s)[0])
