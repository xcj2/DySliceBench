#ABC170 D
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
a = list(map(int,readline().split()))
a.sort()

if a[0] == a[-1]: # n=1 やサンプル２のような時
  if n > 1:
    print(0)
  else:
    print(1)
  exit()

if a[0] == 1: #１だけは素因数分解するときにバグるので別で処理
  if a[0] == a[1]:
    print(0)
  else:
    print(1)
  exit()
  
def divisorize(fct): # 約数のリストつくるやつ
    b, e = fct.pop()
    pre_div = divisorize(fct) if fct else [[]]
    suf_div = [[(b, k)] for k in range(e + 1)]
    return [pre + suf for pre in pre_div for suf in suf_div]

def factorize(n): #素因数分解
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
    
s = set()
ans = 0
for nm,i in enumerate(a):
  c = set()
  fct = factorize(i)
  for div in divisorize(fct): # 約数の集合を作る
      c.add(num(div))

# 積集合をとり、それが空でかつ同じ数字が並んでない時に答えを加算
  if c&s == set() and ((nm < n-1 and a[nm+1] != i) or nm == n-1): 
    ans += 1
  s.add(i) #今まで見た数の集合を更新

print(ans)