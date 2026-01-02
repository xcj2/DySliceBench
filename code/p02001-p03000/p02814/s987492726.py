def gcd(a: int, b: int) -> int:
    """a, bの最大公約数(greatest common divisor:GCD)を求める
    計算量: O(log(min(a, b)))
    """
    if b == 0:
        return a
    return gcd(b, a%b)


def lcm(a, b):
    """a, bの最小公倍数(least common multiple:LCM)を求める
    計算量: O(log(min(a, b)))"""
    return (a * b) // gcd(a, b)

             
def multi_lcm(array, m):
    """arrayのLCMを求める"""
    ans = array[0] 
    for i in range(1, len(array)):
        ans = (ans * array[i]) // gcd(ans, array[i])
        if ans > 5*m:
            return 5*m
    return ans 

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

l = [0] * n
for i in range(n):
    cnt = 0
    tmp = a[i]
    while True:
        if tmp % 2 == 0:
            cnt += 1
            tmp //= 2
        else:
           break
    l[i] = cnt
if max(l) != min(l):
    print(0)
    exit()
    
div = multi_lcm(a, m)
ans = 0
if m - div // 2 >= 0:
    ans += 1
m = m - div // 2 
ans += m // div
if m < 0:
    print(0)
else:
    print(ans)
