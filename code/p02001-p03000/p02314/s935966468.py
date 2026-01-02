#  http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=jp
#  Coin Changing Problem : python3
#  2018.12.11 yonezawa

#from collections import deque
import sys
input = sys.stdin.readline
#import cProfile
#from math import cos,sin,radians,sqrt

def Reflection(p1,p2):
    (x,y) = p2
    (tx,ty) = Projection(p1,(x,y))
    rx = (tx - x) * 2 + x 
    ry = (ty - y) * 2 + y
    return (rx,ry)


def solve(cn:int,l:list):
    calc = [[0 for i in range(len(l))] for j in range(cn+1)]
    calc[0][0] = 0

    for i in range(cn+1):
        calc[i][0] = i // l[0] if i % l[0] == 0 else (i // l[0]) + 1

    for j in range(1,len(l)):
        for i in range(cn+1):
            if i-l[j] >= 0:
                calc[i][j] = min(calc[i][j-1],calc[i-l[j]][j]+1)
            else:
                calc[i][j] = calc[i][j-1]
    print (calc[cn][j])
    return 0

def main():
    (cn,n) = map(int,input().split())
    l = list(map(int,input().split()))

    solve(cn,l)
    
if __name__ == '__main__':
    main()
    #pr = cProfile.Profile()
    #pr.runcall(main)
    #pr.print_stats()
