import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())
def main():
    n = I()
    a = LI()
    a4, a2, a1 = [0 for _ in range(3)]
    for i in a:
        if i%4 == 0:
            a4 += 1
        elif i%2 == 0:
            a2 += 1
        else:
            a1 += 1
    if a1 == 0:
        print("Yes")
    else:
        if a4 == 0:
            print("No")
        elif a2 == 0:
            print("Yes" if a4 >= a1 -1 else "No")
        else:
            print("Yes" if a4 >= a1 else "No")
main()