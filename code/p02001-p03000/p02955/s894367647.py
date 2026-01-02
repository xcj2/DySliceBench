import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,k = map(int,input().split())
a = [int(i) for i in input().split()]

def divisorize(fct):
    b, e = fct.pop()
    pre_div = divisorize(fct) if fct else [[]]
    suf_div = [[(b, k)] for k in range(e + 1)]
    return [pre + suf for pre in pre_div for suf in suf_div]
 
 
def factorize(n):
    fct = []
    b, e = 2, 0
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct
 
 
def num(fct):
    a = 1
    for base, exponent in fct:
        a = a * base**exponent
    return a

c = []
fct = factorize(sum(a))
for div in divisorize(fct):
    c.append(num(div))

c.sort(reverse=True)
ans = 1
from heapq import heapify,heappush,heappop

for num in c:
  chk = 0; cnt = 0
  sp = 0
  pl = []; mi = []
  heapify(pl); heapify(mi)
  for j in a:
    m = min(j%num,num-j%num)
    chk += m
    if m == j%num:
      cnt += m
      heappush(pl,-m)
    else:
      cnt -= m
      heappush(mi,-m)
  
  if cnt != 0:
    for i in range(abs(cnt)//num):
      if cnt > 0 and pl!=[]:
        p = heappop(pl)
        chk += (num+2*p)
      elif cnt < 0 and mi!=[]:
        q = heappop(mi)
        chk += (num+2*q)
        
  if chk <= 2*k:
    ans = num
    break
    
print(ans)