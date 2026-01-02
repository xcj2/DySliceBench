def inp():
    return input()
def iinp():
    return int(input())
def inps():
    return input().split()
def miinps():
    return map(int,input().split())
def linps():
    return list(input().split())
def lmiinps():
    return list(map(int,input().split()))
def lmiinpsf(n):
    return [list(map(int,input().split()))for _ in range(n)]


n,m = miinps()
k = lmiinpsf(m)
a = lmiinps()

ans = 0

for i in range(2**n):
  d = []
  p = len(bin(i))
  q = bin(i)
  for j in range(p-2):
    q = bin(i>>j)
    if int(q[len(q)-1]) == 1:
      d.append(j)
    
  count2 = 0 #点灯している電球の数
  
  for j in range(m):
    count1 = 0 #電球に接続されているスイッチの内onになっている数
    for l in range(len(k[j])-1):
      if (k[j][l+1]-1) in d:
        count1 += 1
    count1 %= 2
    if count1 == a[j]:
      count2 += 1
    else:
      break;
  if count2 == m:
    ans += 1

print(ans)