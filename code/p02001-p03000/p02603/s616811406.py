#関数リスト
import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

n = I()
mylist = LI()
buy = [0] * n

katamuki = 0
for i in range(n-1):
    if katamuki == 0:
        if mylist[i+1] > mylist[i]:
            buy[i] = "buy"
            katamuki = 1
        elif mylist[i+1] < mylist[i]:
            katamuki = -1
    elif katamuki == -1 and mylist[i+1] > mylist[i]:
        buy[i] = "buy"
        katamuki = 1
    elif katamuki == 1 and mylist[i+1] < mylist[i]:
        buy[i] = "sell"
    elif katamuki == 1 and mylist[i+1] > mylist[i]:
        buy[i] = "buysell"

        
result = 1000
stock = 0
price = 0    
for i in range(n):
    if buy[i] == "buy":
        stock = result // mylist[i]
        result -= mylist[i] * stock
    elif buy[i] == "sell":
        result += mylist[i] * stock
        stock = 0
    elif buy[i] == "buysell":
        result += mylist[i] * stock
        stock = result // mylist[i]
        result -= mylist[i] * stock
    elif i == n-1:
        result += mylist[i] * stock
print(result)