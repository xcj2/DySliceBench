import sys
MAX_INT = int(10e15)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def judge(x):
  cnt = 0
  for i in range(N):
    tmp = a[i] - x//f[i]
    cnt += max(tmp, 0)
  else:
    if cnt <= K:
      return True
    else:
      return False

# 二分探索 #
def nibutan(): # MAX(A*F) ans
    left = -1
    ans = num
    while left+1 != ans:
        middle = (left+ans)//2
        if judge(middle):
            ans = middle
        else:
            left = middle
    return ans

N, K = IL()
a = IL()
f = IL()
a.sort()
f.sort(reverse=True)
num = 0
for i in range(N):
  num = max(num, a[i]*f[i])

print(nibutan())
