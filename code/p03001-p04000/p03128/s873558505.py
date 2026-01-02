N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
#from functools import reduce
import copy

cost = [0,2,5,5,4,5,6,3,7,6]

dic = {}
def dic_add(dic, key, val):
  if key in dic:
    dic[key] += adic
def dic_pop(dic, key):
  if key in dic:
    dic.pop(key)
  
for a in A:
  dic[cost[a]] = a
if 2 in dic:
  dic_pop(dic,4)
  dic_pop(dic,6)
  if 3 in dic:
    dic_pop(dic,5)
    dic_pop(dic,7)
  elif 5 in dic:
    dic_pop(dic,7)
elif 3 in dic:
  dic_pop(dic,6)
  if 4 in dic:
    dic_pop(dic,7)

dic_inv = [0 for _ in range(10)]
A = []
for c in dic:
  dic_inv[dic[c]] = c 
  A.append(dic[c])
A.sort(reverse = True)
label = [-1 for _ in range(10)]
for i in range(len(A)):
  label[A[i]] = i
  
def larger(a_lis, b_lis): # a > b の判定
  if sum(a_lis) > sum(b_lis):
    del b_lis
    return a_lis
  elif sum(a_lis) < sum(b_lis):
    del a_lis
    return b_lis
  else:
    if a_lis > b_lis:
      del b_lis
      return a_lis
    else:
      del a_lis
      return b_lis
INF = 10**20
DP = [[-INF for a in A] for _ in range(N+1)]
DP[0] = [0 for a in A]
for n in range(2,N+1):
  for a in A:
    if n - cost[a] >= 0:
      tmp = copy.copy(DP[n - cost[a]])
      tmp[label[a]] += 1
      DP[n] = larger(DP[n], tmp)
      
ans = 0
for a in A:
  num_a = DP[N][label[a]] 
  for i in range(num_a):
    ans *= 10
    ans += a 
    
print(ans)
"""
print(A)
print(label)
print(*DP, sep = "\n")
"""
  
  
      
      
      
  
    
  
  