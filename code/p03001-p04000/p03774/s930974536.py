import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n,m = LI()
    student = []
    spot = []
    for _ in range(n):
        a,b = LI()
        student.append([a,b])

    for _ in range(m):
        c,d = LI()
        spot.append([c,d])
    inf = float("inf")
    for x,y in student:
        near = (0,inf)
        area_num = 1
        for s,t in spot:
            dist = abs(x-s) + abs(y-t)
            if near[1] > dist:
                near = (area_num,dist)
            area_num += 1
        print(near[0])
main()