import sys
input = sys.stdin.readline
import math

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

N, K = MI()
mylist = LI()
length = len(mylist)

high = max(mylist)+1
low = 0
mid = (high + low) / 2

while high - low >= 0.001:
    temp = 0
    for i in mylist:
        if i % mid == 0:
            temp += (i // mid) - 1
        else:
            temp += i // mid
    if temp > K:
        low = mid
    else:
        high = mid
    mid = (high + low) / 2

result = math.ceil(low)


num2 = result+10**(-8)
temp= 0
for i in mylist:
    if i % num2 == 0:
        temp += (i // num2) - 1
    else:
        temp += i // num2
if temp > K:
    print(result+1)
else:
    print(result)