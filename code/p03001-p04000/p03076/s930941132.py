import math
import string


def readints():
    return list(map(int, input().split()))


def nCr(n, r):
    return math.factorial(n)//math.factorial(n-r)*math.factorial(r)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
# 最後に注文する料理は調理時間そのままの時間がかかるので「（x以上最小の10の倍数）とxの差」が最大になるような料理を選ぶと最短の時間になる


def maxtime(x):
    # 調理時間x分の料理について,注文してから次の注文までの時刻は「x以上最小の10の倍数分」
    return int(-(-x//10)*10)


def remtime(x):
    return int(maxtime(x)-x)


sum = 0
sum = int(maxtime(a)+maxtime(b)+maxtime(c)+maxtime(d)+maxtime(e))
sum -= int(max({remtime(a), remtime(b), remtime(c), remtime(d), remtime(e)}))
print(sum)
