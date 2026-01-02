import sys
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def combi(n, r):
  if n - r < r: r = n - r
  if r == 0: return 1
  if r == 1: return n
  numerator = [n - r + k + 1 for k in range(r)]
  denominator = [k + 1 for k in range(r)]
  for p in range(2,r+1):
    pivot = denominator[p - 1]
    if pivot > 1:
      offset = (n - r) % p
      for k in range(p-1,r,p):
        numerator[k - offset] /= pivot
        denominator[k] /= pivot
  result = 1
  for k in range(r):
    if numerator[k] > 1:
      result *= int(numerator[k])
  return result

N = I()
data = []

for _ in range(N):
  s = [i for i in S()]
  s.sort()
  data.append("".join(map(str,s)))

data.sort()
#print(data)

tmp = ""
cnt = 0
num = 1
for i in range(N):
  #print(tmp)
  if tmp == data[i]:
    num += 1
    continue
  else:
    if num != 1:
      cnt += combi(num,2)
    tmp = data[i]
    num = 1
  #print(cnt)
else:
  if num != 1:
    cnt += combi(num,2)
  tmp = data[i]
  num = 1

print(cnt)