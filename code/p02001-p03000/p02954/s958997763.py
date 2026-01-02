import sys
MAX_INT = int(10e9)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def judge(a,b,i,left,right):
  if (a+b)%2 == 0:
    ans[left] = (a+b)//2
    ans[right] = (a+b)//2
  else:
    num = (a+b)//2
    num2 = (a+b)-(a+b)//2
    if a >= b:
      if (a-1)%2 == 0:
        ans[left] = num2
        ans[right] = num
      else:
        ans[left] = num
        ans[right] = num2
    else:
      if (b-1)%2 == 0:
        ans[left] = num
        ans[right] = num2
      else:
        ans[left] = num2
        ans[right] = num

s = S()
N = len(s)
ans = [0]*N

r = 0
l = 0
f = 0

ll = 0
rr = 0
for i in range(N):
  if f == 0:
    if s[i] == "R":
      r += 1
    else:
      l += 1
      f = 1
      if s[i-1] == "R":
        rr = i-1
        ll = i
  else:
    if s[i] == "R":
      judge(r,l,i,rr,ll)
      r = 0
      l = 0
      r += 1
      f = 0
      indef = 0
    else:
      l += 1
      f = 1
else:
  judge(r,l,i,rr,ll)

print(" ".join(map(str,ans)))