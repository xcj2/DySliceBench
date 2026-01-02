import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    a = LI()
    dic = collections.Counter(a)
    als = 0
    exl = [0 for _ in range(n+1)]
    for key, value in dic.items():
        if value >= 3:
            choice = (value)*(value-1)//2
            choice1 = (value-1)*(value-2)//2
            als += choice
            exl[key] = choice1 - choice
        elif value == 2:
            choice = (value)*(value-1)//2
            als += choice
            exl[key] = -choice
    
    for ball in a:
        choices = als + exl[ball]
        print(choices)
main()            
