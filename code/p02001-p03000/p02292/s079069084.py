#  http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_1_C&lang=jp
#  Counter-Clockwise : python3
#  2018.12.11 yonezawa

#from collections import deque
import sys
input = sys.stdin.readline
#import cProfile
from math import cos,sin,radians,sqrt

def crossProduct(s1,s2,s3):
    (x1,y1) = s1
    (x2,y2) = s2
    (x3,y3) = s3
    x1 = x1 - x2
    y1 = y1 - y2
    x3 = x3 - x2
    y3 = y3 - y2
    d = x1 * y3 - y1 * x3
    return d
def distance(s1,s2):
    (x1,y1) = s1
    (x2,y2) = s2
    return sqrt(pow((x1-x2),2) + pow((y1-y2),2))

    

    

def main():
    (x1,y1,x2,y2) = map(int,input().split())
    for i in range(int(input())):
        (x3,y3) = map(int,input().split())
        n = crossProduct((x1,y1),(x2,y2),(x3,y3))
        if n == 0:
            d1 = distance((x1,y1),(x2,y2))
            d2 = distance((x1,y1),(x3,y3))
            d3 = distance((x2,y2),(x3,y3))
            #print (d1,d2,d3,"p1:",x1,y1,"p2:",x2,y2,"p3:",x3,y3)
            #print (round(d1+d2,10),round(d3,10))
            if round(d1 + d2,5) == round(d3,5) and d1 != 0 and d2 != 0:
                print ("ONLINE_BACK")
            elif d1 >= d2 :
                print ("ON_SEGMENT")
            else:
                print ("ONLINE_FRONT")
        elif n > 0:
            print ("CLOCKWISE") 
        elif n < 0:
            print ("COUNTER_CLOCKWISE")


if __name__ == '__main__':
    main()
    #pr = cProfile.Profile()
    #pr.runcall(main)
    #pr.print_stats()
