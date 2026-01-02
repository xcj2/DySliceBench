from sys import stdin, stderr, setrecursionlimit, exit
setrecursionlimit(2147483647)
def getint():
    return int(stdin.readline().rstrip('\r\n'))
def getints():
    return [int(i) for i in stdin.readline().rstrip('\r\n').split()]
def getintlines():
    return [int(i) for i in stdin.readlines()]
def getintslines():
    return [[int(i) for i in s.split()] for s in stdin.readlines()]
def debug(*args, **kwargs):
    print(*args, file=stderr, **kwargs)

n, m = getints()
shops = getintslines()

shops.sort(key=lambda x:x[0])
current_drink = 0
current_money = 0
for price, num in shops:
    current_money += price * num if current_drink + num <= m else price * (m - current_drink)
    current_drink += num
    if current_drink >= m:
        break
    
print(current_money)

