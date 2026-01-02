import sys
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def cnt(l):
  num = 1
  for i in l:
    if i != s:
      num *= (i+1)
  return num

N = I()
s = S()

dic = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,\
  "l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,\
    "x":0,"y":0,"z":0,}

ans = 0
for i in range(N):
  ans += cnt(list(dic.values()))//(dic[s[i]]+1)
  dic[s[i]] += 1

print(ans%mod)