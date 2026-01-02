import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    a = LI()

    money = 1000
    mn, mx = a[0], a[0]
    up = True

    for price in a:
        if mx <= price:
            up = True
            mx = price
        else:
            if up:
                money = money//mn * mx + money%mn
            up = False
            mn, mx = price, price

    money = money//mn * mx + money%mn
    
    print(money)
            

main()
