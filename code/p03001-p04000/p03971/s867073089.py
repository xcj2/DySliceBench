import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())
def main():
    n,a,b = LI()
    s = S()
    cnt = 1
    cntb = 1

    for i in s:
        if i == "a":
            if cnt<=a+b:
                print("Yes")
                cnt+=1
            else:
                print("No")
        elif i == "b":
            if cnt<=a+b and cntb<=b:
                print("Yes")
                cnt+=1
                cntb+=1
            else:
                print("No")
        else:
            print("No")
main()