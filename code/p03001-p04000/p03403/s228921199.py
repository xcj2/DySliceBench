import math
def MI(): return map(int, input().split())
def II(): return int(input())
def IS(): return input()
def LI(): return list(map(int, input().split()))


n = II()
a = LI()
a.insert(0,0)
a.append(0)
diff = [abs(a[i] - a[i-1]) for i in range(1,len(a))]
money = sum(diff)
# print(a)
# print(diff)
for i in range(1,len(a)-1):
    if a[i-1] <= a[i] <= a[i+1]:
        print(money)
    elif a[i+1] <= a[i] <= a[i-1]:
        print(money)
    elif a[i] <= a[i-1] <= a[i+1]:
        print(money-2*abs(a[i-1]-a[i]))
    elif a[i+1] <= a[i-1] <= a[i]:
        print(money-2*abs(a[i-1]-a[i]))
    elif a[i-1] <= a[i+1] <= a[i]:
        print(money-2*abs(a[i+1]-a[i]))
    else:
        # a[i] <= a[i+1] <= a[i-1]
        print(money-2*abs(a[i+1]-a[i]))
