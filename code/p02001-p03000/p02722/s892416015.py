#ABC161-F Division or Substraction
"""
nとn-1の約数の個数が答え
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())

"""約数の個数"""
#参考：青チャp280
#注意：1も約数としてカウントされる
def factrize(n):
    b = 2
    fct = []
    while b*b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b+1
    if n > 1:
        fct.append(n)
    if len(fct) == 1: #素数だった場合
        return 2 #1と、その数の2通り
    
    divisor = dict()
    for i in fct:
        if not i in divisor:
            divisor[i] = 1
        else:
            divisor[i] += 1
    ans = 1
    for i in divisor.values():
        ans *= (i+1)
    return ans
def factrize_all(n):
    b = 2
    fct = []
    while b*b <= n:
        if n%b == 0:
            fct.append(b)
        b += 1
    return fct + [n]

ans = 0
res2 = []
for i in factrize_all(n):
    res = n
    while True:
        if res == 0:
            break
        if res%i != 0:
            res2.append([i,res])
            break
        res = res//i

for i,j in res2:
    if j%i == 1:
        ans += 1

print(ans+factrize(n-1)-1) #1を2回引く