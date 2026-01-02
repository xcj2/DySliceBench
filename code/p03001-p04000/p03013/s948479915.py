import math
import fractions
import copy
#以下てんぷら
def j(q):
    if q==1: print("YES")
    elif q == 0:print("NO")
    exit(0)
rem = pow(10,9)+7
"""
def ct(x,y):
    if (x>y):print("+")
    elif (x<y): print("-")
    else: print("?")
"""

def ip():
    return int(input())
def printrow(a):
    for i in a:
        print(i)
def combinations(n,r):
    if n<r:return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def permutations(n,r):
    if n<r:return 0
    return math.factorial(n) // math.factorial(n - r)
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)


#n = ip()                                     #入力整数1つ
n,m= (int(i) for i in input().split())       #入力整数横2つ以上
#a = [int(i) for i in input().split()]        #入力整数配列
#a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列
#n = ip()                      #入力セット(整数改行あり)(1/2)
a=[ip() for i in range(m)]    #入力セット(整数改行あり)(2/2)
#a=[input() for i in range(n)]    #入力セット(整数改行あり)(2/2)
#jの変数はしようできないので注意
#全足しにsum変数使用はsum関数使用できないので注意
#a.pop(0)は10^5あるときTLEしやすい!注意!抜くなら逆ソート!
#これを消すとなぜかWAになる呪い
for i in range(m-1):
    if a[i]+1 == a[i+1]:
        print(0)
        exit(0)
if n == 1:
    print(1)
else:
    p = 0
    dp = [0 for i in range(n+1)]
    dp[1]  = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    left = [i+1 for i in a]
    right = [i-1 for i in a]
    left.insert(0,0)
    right.append(n)
    s = 1
    for i in range(len(right)):
        if right[i] != left[i] :s*=dp[right[i]-left[i]]
        s%=rem
    print(s)