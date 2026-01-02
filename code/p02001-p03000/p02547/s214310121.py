import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():


    n = I()
    saikoro = []
    for i in range(n):
        a, b = LI()
        saikoro.append((a, b))

    cnt = 0

    for deme in saikoro:
        if len(set(deme)) == 1:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            print("Yes")
            exit(0)

    print("No")

main()
